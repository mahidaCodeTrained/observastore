from django.shortcuts import render
from .models import StoreGoods

# Create your views here.

def view_store_goods(request):
    """This view is designed to show the 
    products that Observastore will sell."""

    # Get all products
    products = StoreGoods.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'storefront/storefront.html', context)



