from django.test import TestCase
from .models import StoreGoods, Category

# Create your tests here.


class StoreGoodsTesting(TestCase):
    """ I am testing the StoreGoods model to make sure that the model behaves 
    as intended."""

    def setUp(self):
        # Creating setUp for easy use of unittesting to avoid repeating code.
        self.category = Category.objects.create(name="Telescopes")

        # Creating a sample of the model to test.
        self.product = StoreGoods.objects.create(
            category=self.category,
            sku="12345",
            name="Telescope",
            description="A high-quality telescope for stargazing.",
            price="199.99",
            weight=None,
            image=None
        )

    def test_storegoods_created(self):
        self.assertEqual(self.product.name, "Telescope")
        self.assertEqual(self.product.sku, "12345")
        self.assertEqual(self.product.price, "199.99")
        self.assertEqual(self.product.category.name, "Telescopes")
        self.assertEqual(self.product.weight, None)
