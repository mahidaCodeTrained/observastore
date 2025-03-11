from django.shortcuts import render, get_object_or_404, redirect
from storefront.models import StoreGoods
from django.contrib import messages
from .contexts import bag_contents


def view_shopping_bag(request):
    """
    View to display the contents of the shopping bag.
    """
    # Retrieve the shopping bag from the session, if it exists
    # The context processor is handling all the logic now, so we simply call the bag_contents function
    context = bag_contents(request)  # This calls the context processor

    return render(request, 'bag/shopping_bag.html', context)


def add_to_bag(request, item_id):
    """
    Add a specified quantity of a product to the shopping bag.
    """
    product = get_object_or_404(StoreGoods, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1 if not provided
    redirect_url = request.POST.get('redirect_url', '')  # URL to redirect after adding to bag

    # Get the current shopping bag from the session (or an empty dictionary if it doesn't exist)
    bag = request.session.get('bag', {})

    # Check if the item is already in the bag
    if str(item_id) in bag:
        bag[str(item_id)] += quantity
        messages.success(request, f'Updated quantity for "{product.name}" to {bag[str(item_id)]}')
    else:
        bag[str(item_id)] = quantity
        messages.success(request, f'Added "{product.name}" to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url or 'storefront')





