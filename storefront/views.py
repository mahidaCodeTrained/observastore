from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import StoreGoods, Category


def view_store_goods(request):
    """This view is designed to show the products that Observastore will sell."""

    # Get all products
    products = StoreGoods.objects.all()
    query = None
    categories = None
    category_name = None  # New variable to store category name for display
    sort_by = request.GET.get('sort', '')  # Get the sorting parameter from the request

    if request.GET:
        # Apply category filter
        if 'category' in request.GET:
            categories_param = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories_param)
            categories = Category.objects.filter(name__in=categories_param)
            category_name = ', '.join([cat.name for cat in categories])  # Format category names for display

        # Apply search filter
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('storefront'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = StoreGoods.objects.filter(queries)

        # Apply sorting
        if sort_by == 'price_asc':
            products = products.order_by('price')  # Sort by price low to high
        elif sort_by == 'price_desc':
            products = products.order_by('-price')  # Sort by price high to low
        elif sort_by == 'weight_asc':
            products = products.order_by('weight')  # Sort by weight low to high
        elif sort_by == 'weight_desc':
            products = products.order_by('-weight')  # Sort by weight high to low

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,  # Will be None if no category filter is applied
        'category_name': category_name,  # Pass the category name to template
    }

    return render(request, 'storefront/storefront.html', context)


def detailed_products(request, product_id):

    product = get_object_or_404(StoreGoods, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'storefront/product_details.html', context)

