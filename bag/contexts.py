from decimal import Decimal
from django.conf import settings
from storefront.models import StoreGoods


def bag_contents(request):
    # Retrieve the shopping bag from the session
    bag = request.session.get('bag', {})

    # Variables for bag items and totals
    bag_items = []
    total = 0
    product_count = 0

    for item_id, quantity in bag.items():
        try:
            product = StoreGoods.objects.get(id=item_id)
            total += product.price * quantity
            product_count += quantity

            bag_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': product.price * quantity
            })
        except StoreGoods.DoesNotExist:
            continue  # If the product doesn't exist, skip it

    # Calculate delivery and grand total
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # Returning the context with the required values
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

