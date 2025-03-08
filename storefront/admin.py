from django.contrib import admin
from .models import Category, StoreGoods


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'visual_name')
    search_fields = ('name', 'visual_name')


@admin.register(StoreGoods)
class StoreGoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'sku', 'weight')
    list_filter = ('category', 'price')
    search_fields = ('name', 'description', 'sku')
