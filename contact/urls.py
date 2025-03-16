from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact_form'),
    path('subscribe/', views.newsletter_subscribe,
         name='newsletter_subscribe'),
]
