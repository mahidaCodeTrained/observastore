from django.test import TestCase
from django.urls import reverse
from storefront.models import StoreGoods
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages import get_messages


class ShoppingBagTests(TestCase):
    def setUp(self):
        # Create a product with size and a product without size
        self.product_with_size = StoreGoods.objects.create(
            name="T-shirt Large",
            price=20.00,
            sizes=True,
            description="A large-sized t-shirt",
        )
        self.product_without_size = StoreGoods.objects.create(
            name="T-shirt",
            price=15.00,
            sizes=False,
            description="A plain t-shirt",
        )
    
    def add_product_to_bag(self, product, quantity=1, size=None):
        """ Helper function to add a product to the bag """
        url = reverse('add_to_bag', args=[product.id])
        data = {'quantity': quantity}
        if size is not None:
            data['size'] = size
        response = self.client.post(url, data=data)
        return response

    def test_add_to_bag_without_size(self):
        """ Test adding a product without size to the shopping bag """
        response = self.add_product_to_bag(self.product_without_size)
        self.assertEqual(response.status_code, 302)

        bag = self.client.session.get('bag', {})
        self.assertIn(str(self.product_without_size.id), bag)
        self.assertEqual(bag[str(self.product_without_size.id)], 1)

    def test_add_to_bag_with_size(self):
        """ Test adding a product with size to the shopping bag """
        response = self.add_product_to_bag(self.product_with_size, size="L")
        self.assertEqual(response.status_code, 302)
        bag = self.client.session.get('bag', {})
        self.assertIn(str(self.product_with_size.id), bag)
        self.assertIn("items_by_size", bag[str(self.product_with_size.id)])
        self.assertIn("L", bag[str(self.product_with_size.id)]["items_by_size"])
        self.assertEqual(bag[str(self.product_with_size.id)]["items_by_size"]["L"], 1)

    def test_adjust_bag_with_size(self):
        """ Test adjusting the quantity of a product with size in the bag """
        self.add_product_to_bag(self.product_with_size, size="L")
        
        url = reverse('adjust_bag', args=[self.product_with_size.id])
        response = self.client.post(url, data={'quantity': 3, 'product_size': 'L'})
        self.assertEqual(response.status_code, 302)

        bag = self.client.session.get('bag', {})
        self.assertEqual(bag[str(self.product_with_size.id)]["items_by_size"]["L"], 3)

    def test_adjust_bag_without_size(self):
        """ Test adjusting the quantity of a product without size in the bag """
        # Add product without size to bag first
        self.add_product_to_bag(self.product_without_size)
        
        # Adjust the quantity of the product in the bag
        url = reverse('adjust_bag', args=[self.product_without_size.id])
        response = self.client.post(url, data={'quantity': 5})
        self.assertEqual(response.status_code, 302)

        # Check if the quantity was updated
        bag = self.client.session.get('bag', {})
        self.assertEqual(bag[str(self.product_without_size.id)], 5)
    
    def test_bag_with_multiple_sizes(self):
        """ Test adding multiple sizes of the same product to the bag """
        self.add_product_to_bag(self.product_with_size, quantity=1, size="M")
        self.add_product_to_bag(self.product_with_size, quantity=1, size="L")
        
        bag = self.client.session.get('bag', {})
        self.assertIn(str(self.product_with_size.id), bag)
        self.assertEqual(len(bag[str(self.product_with_size.id)]["items_by_size"]), 2)
        self.assertEqual(bag[str(self.product_with_size.id)]["items_by_size"]["M"], 1)
        self.assertEqual(bag[str(self.product_with_size.id)]["items_by_size"]["L"], 1)


