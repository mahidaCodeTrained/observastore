from django.shortcuts import render, get_object_or_404
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


def detailed_products(request, product_id):

    product = get_object_or_404(StoreGoods, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'storefront/product_details.html', context)

