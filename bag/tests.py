from django.test import TestCase
from django.urls import reverse
from storefront.models import StoreGoods, Category
from django.contrib.auth.models import User


class ShoppingBagTests(TestCase):
    def setUp(self):
        """
        Setting up test data.
        """
        # Create category
        self.category = Category.objects.create(name="Telescopes", visual_name="Telescopes")

        # Create a product
        self.product = StoreGoods.objects.create(
            category=self.category,
            sku="12345",
            name="Test Telescope",
            description="A great telescope.",
            price=100.00,
            sizes=True,
            weight=2.5,
        )

        # Create user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Setup session
        self.client.login(username='testuser', password='password')

    def test_add_to_bag(self):
        """
        Test if adding an item to the bag works properly.
        """
        # Add product to bag
        response = self.client.post(reverse('add_to_bag', args=[self.product.id]), {'quantity': 2, 'size': 'Large'})
        self.assertEqual(response.status_code, 302)  # Check redirection
        self.assertIn(str(self.product.id), self.client.session['bag'])
        self.assertEqual(self.client.session['bag'][str(self.product.id)]['items_by_size']['Large'], 2)

    def test_remove_from_bag(self):
        """
        Test removing an item from the bag works correctly.
        """
        self.client.post(reverse('add_to_bag', args=[self.product.id]), {'quantity': 2, 'size': 'Large'})
        self.assertIn(str(self.product.id), self.client.session['bag'])
        self.assertEqual(self.client.session['bag'][str(self.product.id)]['items_by_size']['Large'], 2)

        response = self.client.post(reverse('remove_from_bag', args=[self.product.id]), {'size': 'Large'})

        self.assertNotIn(str(self.product.id), self.client.session['bag'])
        self.assertEqual(response.status_code, 302)  # Check redirection
        self.assertContains(response, 'Removed')
        self.assertNotIn(str(self.product.id), self.client.session['bag'])

    def test_remove_item_with_no_size(self):
        """
        Test removing an item with no size.
        """
        self.client.post(reverse('add_to_bag', args=[self.product.id]), {'quantity': 2})
        self.assertIn(str(self.product.id), self.client.session['bag'])
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 2)

        response = self.client.post(reverse('remove_from_bag', args=[self.product.id]), {'size': ''})  # Passing empty string

        self.assertNotIn(str(self.product.id), self.client.session['bag'])
        self.assertEqual(response.status_code, 302)  # Check redirection
        self.assertNotIn(str(self.product.id), self.client.session['bag'])

