from decimal import Decimal, ROUND_HALF_UP
from django.conf import settings
from storefront.models import StoreGoods


def bag_contents(request):
    # Retrieve the shopping bag from the session
    bag = request.session.get('bag', {})

    # Variables for bag items and totals
    bag_items = []
    total = Decimal('0.00')
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
        delivery = (total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        free_delivery_delta = (settings.FREE_DELIVERY_THRESHOLD - total).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = (total + delivery).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    # Returning the context with the required values
    context = {
        'bag_items': bag_items,
        'total': total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context


