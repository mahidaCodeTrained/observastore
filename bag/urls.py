from django.urls import path
from . import views

urlpatterns = [
    path('add_to_bag/<int:item_id>/', views.add_to_bag, name='add_to_bag'),
    path('', views.view_shopping_bag, name='shopping_bag'),

]