from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, "Update has failed, please ensure that you \
                      have submitted the form correctly.")
    else:
        form = UserProfileForm(instance=profile)
    # Ordering the orders by the date in descending order
    orders = profile.orders.all().order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to view this page.")
        return redirect('login')  # Redirect to login page if not authenticated

    order = get_object_or_404(Order, order_number=order_number)

    # Ensure the order is associated with the logged-in user's profile
    if order.user_profile is None or order.user_profile.user != request.user:
        messages.error(request, "You do not have permission to view this order.")
        return redirect('home')  # Redirect to homepage if the order doesn't belong to the logged-in user

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

