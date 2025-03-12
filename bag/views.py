from django.shortcuts import render, get_object_or_404, redirect, reverse
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
    
    size = request.POST.get('size', None)
    bag = request.session.get('bag', {})

    # If the product has sizes and a size is selected
    if product.sizes and size:  
        if str(item_id) in bag:
            if isinstance(bag[str(item_id)], dict):  # Check if it's a dictionary (items_by_size)
                if 'items_by_size' in bag[str(item_id)]:
                    if size in bag[str(item_id)]['items_by_size']:
                        bag[str(item_id)]['items_by_size'][size] += quantity
                        messages.success(request, f'Updated quantity for "{product.name}" size {size} to {bag[str(item_id)]["items_by_size"][size]}')
                    else:
                        bag[str(item_id)]['items_by_size'][size] = quantity
                        messages.success(request, f'Added "{product.name}" size {size} to your bag')
                else:
                    bag[str(item_id)] = {'items_by_size': {size: quantity}}
                    messages.success(request, f'Added "{product.name}" size {size} to your bag')
            else:
                bag[str(item_id)] = {'items_by_size': {size: quantity}}
                messages.success(request, f'Added "{product.name}" size {size} to your bag')
        else:
            bag[str(item_id)] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added "{product.name}" size {size} to your bag')
    else:
        if str(item_id) in bag:
            if isinstance(bag[str(item_id)], int):  # If it's an integer (no size)
                bag[str(item_id)] += quantity
                messages.success(request, f'Updated quantity for "{product.name}" to {bag[str(item_id)]}')
            elif isinstance(bag[str(item_id)], dict):
                pass
        else:
            bag[str(item_id)] = quantity
            messages.success(request, f'Added "{product.name}" to your bag')

    request.session['bag'] = bag

    return redirect('product_details', product_id=item_id)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})

    if str(item_id) in bag:
        if size:  # Handling for products with sizes
            if 'items_by_size' in bag[str(item_id)]:
                if quantity > 0:
                    bag[str(item_id)]['items_by_size'][size] = quantity
                else:
                    del bag[str(item_id)]['items_by_size'][size]
                    if not bag[str(item_id)]['items_by_size']:
                        del bag[str(item_id)]
            else:
                # Handle case where the product doesn't have 'items_by_size'
                if quantity > 0:
                    bag[str(item_id)] = {'items_by_size': {size: quantity}}
                else:
                    del bag[str(item_id)]
        else:  # Handling for products without sizes
            if quantity > 0:
                bag[str(item_id)] = quantity
            else:
                del bag[str(item_id)]

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def remove_from_bag(request, item_id):
    """Remove a product from the shopping bag."""
    product = get_object_or_404(StoreGoods, pk=item_id)
    size = request.POST.get('product_size', None)  # Get size if the product has sizes
    bag = request.session.get('bag', {})

    if str(item_id) in bag:
        if size and 'items_by_size' in bag[str(item_id)]:
            # If the product has a size and it's in the items_by_size dictionary
            if size in bag[str(item_id)]['items_by_size']:
                del bag[str(item_id)]['items_by_size'][size]
                if not bag[str(item_id)]['items_by_size']:  # If no more sizes left for this product
                    del bag[str(item_id)]
                messages.success(request, f'Removed "{product.name}" size {size} from your bag.')
        else:
            # If no size or just a simple product
            del bag[str(item_id)]
            messages.success(request, f'Removed "{product.name}" from your bag.')

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))






