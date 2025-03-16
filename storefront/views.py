from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import StoreGoods, Category

from .forms import StoreForm


def view_store_goods(request):
    """This view is designed to show the products """

    # Get all products
    products = StoreGoods.objects.all()
    query = None
    categories = None
    category_name = None
    sort_by = request.GET.get('sort', '')

    if request.GET:

        if 'category' in request.GET:
            categories_param = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories_param)
            categories = Category.objects.filter(name__in=categories_param)
            category_name = ', '.join([cat.name for cat in categories])

        # Apply search filter if present
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('storefront'))
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = StoreGoods.objects.filter(queries)

        if sort_by == 'price_asc':
            products = products.order_by('price')
        elif sort_by == 'price_desc':
            products = products.order_by('-price')
        elif sort_by == 'weight_asc':
            products = products.order_by('weight')
        elif sort_by == 'weight_desc':
            products = products.order_by('-weight')
        elif sort_by == 'name_asc':
            products = products.order_by('name')
        elif sort_by == 'name_desc':
            products = products.order_by('-name')

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'category_name': category_name,
        'sort_by': sort_by,
    }

    return render(request, 'storefront/storefront.html', context)


def detailed_products(request, product_id):

    product = get_object_or_404(StoreGoods, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'storefront/product_details.html', context)


@login_required
def add_product(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added your new product!")
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request, "Failed to add your new product please check \
                that the form is valid")
    else:
        form = StoreForm()
    template = 'storefront/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(StoreGoods, pk=product_id)
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                           Please ensure the form is valid.')
    else:
        form = StoreForm(instance=product)
        messages.info(request, f'You are editing the\
                       product called... {product.name}')

    template = 'storefront/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(StoreGoods, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('storefront'))
