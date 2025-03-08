from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_store_goods, name='storefront'),
    path('<product_id>', views.detailed_products, name='product_details'),

]