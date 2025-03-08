from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_store_goods, name='storefront'),

]