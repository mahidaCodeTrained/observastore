from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import StoreGoods, Category


class StoreGoodsViewTests(TestCase):
    def setUp(self):
        self.category_telescopes = Category.objects.create(name='Telescopes')
        self.category_globes = Category.objects.create(name='Globes')

        self.product1 = StoreGoods.objects.create(
            name='Telescope A',
            description='A great telescope.',
            price=100.00,
            category=self.category_telescopes
        )
        self.product2 = StoreGoods.objects.create(
            name='Globe A',
            description='A beautiful globe.',
            price=50.00,
            category=self.category_globes
        )

        self.product3 = StoreGoods.objects.create(
            name='Telescope B',
            description='Another great telescope.',
            price=120.00,
            category=self.category_telescopes
        )

    def test_view_store_goods(self):

        response = self.client.get(reverse('storefront'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Our Products')
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)

    def test_view_store_goods_with_category_filter(self):

        response = self.client.get(reverse('storefront') + '?category=Telescopes')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product3.name)
        self.assertNotContains(response, self.product2.name)
    
    def test_view_store_goods_with_search(self):
        response = self.client.get(reverse('storefront') + '?q=Telescope A')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Telescope A')
        self.assertNotContains(response, 'Globe A')

    def test_detailed_product_view(self):
        response = self.client.get(reverse('product_details', args=[self.product1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product1.description)
        self.assertContains(response, f"${self.product1.price}")





