from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from storefront.models import StoreGoods


def view_shopping_bag(request):
    """
    View to display the contents of the shopping bag.
    """
    # Retrieve the shopping bag from the session, if it exists
    bag = request.session.get('bag', {})

    # Create a list of the products in the bag and their quantities
    bag_items = []
    total_price = 0

    for item_id, quantity in bag.items():
        try:
            # Fetch the product from the database using the item_id from the bag
            product = StoreGoods.objects.get(id=item_id)
            product_total = product.price * quantity  # Price * Quantity for each item
            total_price += product_total

            # Add the product details, quantity, and total price for this item to the list
            bag_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': product_total
            })
        except StoreGoods.DoesNotExist:
            continue  # Skip if the product doesn't exist (though ideally it shouldn't happen)


    context = {
        'bag_items': bag_items,
        'total_price': total_price
    }

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




