from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import StoreGoods

# Create your views here.


def view_store_goods(request):
    """This view is designed to show the 
    products that Observastore will sell."""

    # Get all products
    products = StoreGoods.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('storefront'))                    
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = StoreGoods.objects.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'storefront/storefront.html', context)


def detailed_products(request, product_id):

    product = get_object_or_404(StoreGoods, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'storefront/product_details.html', context)

