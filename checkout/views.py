from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('storefront'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51R2Fg6C0DsChuQrL64oyDgZcxzrFDpIb3yUZlOPfkyFKYVJPy7WG1vSvnzkEpMtpfEX7RaoST4ZiV2m4ZKatiEud00pqOpAqnL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
