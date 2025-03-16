from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import ContactRequest
from storefront.models import StoreGoods

class ContactViewTest(TestCase):
    def setUp(self):

        self.product = StoreGoods.objects.create(name='Test Product', price=100.0)

    def test_contact_view_post_valid_form(self):
        """Test that submitting a valid contact form redirects and saves data."""
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'store_good': self.product.id,
            'message': 'Hello, this is a test message.'
        }

        response = self.client.post(reverse('contact_form'), form_data, follow=True)

       
        messages = list(get_messages(response.wsgi_request))
 
        self.assertTrue(any("Thank you for contacting us!" in str(msg) for msg in messages))

        self.assertTrue(ContactRequest.objects.filter(email='johndoe@example.com').exists())




