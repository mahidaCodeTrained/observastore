from django.shortcuts import render, get_object_or_404, redirect
from storefront.models import StoreGoods
from django.contrib import messages
from .contexts import bag_contents


def view_shopping_bag(request):
    """
    View to display the contents of the shopping bag.
    """
    # Retrieve the shopping bag from the session, if it exists
    context = bag_contents(request)

    return render(request, 'bag/shopping_bag.html', context)


def add_to_bag(request, item_id):
    """
    Add a specified quantity of a product to the shopping bag.
    """
    product = get_object_or_404(StoreGoods, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '')
    
    size = request.POST.get('size', None)
    bag = request.session.get('bag', {})

    if product.sizes and size:  # If product has sizes, and a size is selected
        if str(item_id) in bag:
            if 'items_by_size' in bag[str(item_id)]:
                if size in bag[str(item_id)]['items_by_size']:
                    bag[str(item_id)]['items_by_size'][size] += quantity
                    messages.success(request, f'Updated quantity for "{
                        product.name}" size {size} to {bag[str(item_id)]["items_by_size"][size]}')
                else:
                    bag[str(item_id)]['items_by_size'][size] = quantity
                    messages.success(request, f'Added "{product.name}" size {size} to your bag')
            else:
                bag[str(item_id)] = {'items_by_size': {size: quantity}}
                messages.success(request, f'Added "{product.name}" size {size} to your bag')
        else:
            bag[str(item_id)] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added "{product.name}" size {size} to your bag')
    else:  # If the product doesn't have sizes, just add it normally
        if str(item_id) in bag:
            bag[str(item_id)] += quantity
            messages.success(request, f'Updated quantity for "{product.name}" to {bag[str(item_id)]}')
        else:
            bag[str(item_id)] = quantity
            messages.success(request, f'Added "{product.name}" to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url or 'storefront')





