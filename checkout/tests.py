from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from unittest.mock import patch
from .models import Order
from profiles.models import UserProfile
from storefront.models import StoreGoods

class CheckoutSuccessTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user and profile for testing
        cls.user = User.objects.create_user(username='testuser', password='password')
        cls.profile = UserProfile.objects.create(user=cls.user)

        # Create a test product and add it to the cart
        cls.product = StoreGoods.objects.create(name="Test Product", price=10.0)

        # Create an order
        cls.order = Order.objects.create(
            user=cls.user,
            stripe_pid="test_pid",
            original_bag="{}",
            full_name="Test User",
            email="test@example.com",
            phone_number="1234567890",
            country="Test Country",
            postcode="12345",
            town_or_city="Test City",
            street_address1="Test Street 1",
            street_address2="Test Street 2",
            county="Test County",
        )

    @patch('profiles.models.UserProfile.save')
    def test_checkout_success_authenticated_user(self, mock_save):
        # Simulate the GET request for checkout_success view
        response = self.client.get(reverse('checkout_success', args=[self.order.order_number]))

        # Check that the order is retrieved correctly
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.order_number)

        # Check if the user profile is attached to the order
        self.order.refresh_from_db()  # Ensure we get the updated order from the database
        self.assertEqual(self.order.user_profile, self.profile)

        # Check the success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f"Order successfully processed! Your order number is {self.order.order_number}. A confirmation email will be sent to {self.order.email}.")

        # Ensure the user profile save method was called
        mock_save.assert_called_once()

    @patch('profiles.models.UserProfile.save')
    def test_checkout_success_no_authenticated_user(self, mock_save):
        # Simulate the GET request for checkout_success without logging in
        self.client.logout()
        response = self.client.get(reverse('checkout_success', args=[self.order.order_number]))

        # Check that the order is retrieved correctly
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.order_number)

        # Ensure the user profile save method was not called (no authenticated user)
        mock_save.assert_not_called()

        # Check the success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f"Order successfully processed! Your order number is {self.order.order_number}. A confirmation email will be sent to {self.order.email}.")

    def tearDown(self):
        # Delete the created objects after each test to avoid conflicts
        self.user.delete()
        self.profile.delete()
        self.product.delete()
        self.order.delete()


