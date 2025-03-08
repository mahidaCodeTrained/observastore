from django.test import TestCase
from django.urls import reverse
from .models import StoreGoods, Category
from django.contrib.auth import get_user_model


class ProductDetailViewTestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.product = StoreGoods.objects.create(
            name='Test Product',
            description='A test product for testing.',
            price=99.99,
        )
        
    def test_product_detail_view(self):
        """Test that the product details page renders correctly."""
        
        url = reverse('product_details', kwargs={'product_id': self.product.id})  # Change this line
        
        response = self.client.get(url)
        
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        
        #  Im Checking that the correct template is used
        self.assertTemplateUsed(response, 'storefront/product_details.html')
        
        # Check that the product data is in the context
        self.assertEqual(response.context['product'], self.product)
        
        # Check that the product's name and description appear in the HTML
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.description)
        self.assertContains(response, str(self.product.price))

    def test_product_not_found(self):
        """Test that trying to view a product that doesn't exist returns a 404."""
        
        url = reverse('product_details', kwargs={'product_id': 9999})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 404)



