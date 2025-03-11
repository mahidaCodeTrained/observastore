from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=254)
    visual_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta():
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_visual_name(self):
        return self.visual_name


class StoreGoods(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sizes = models.BooleanField(default=False, null=True, blank=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)

    class Meta():
        verbose_name_plural = "Store Goods"

    def __str__(self):
        return self.name
