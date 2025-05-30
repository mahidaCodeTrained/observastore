from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactRequestForm, NewsletterForm
from django.template import TemplateDoesNotExist
from .models import Newsletter


def contact_view(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for contacting us! "
                "We will look over your contact request and get back to you!"
            )
            return redirect('contact_form')
    else:
        form = ContactRequestForm()

    try:
        # Just use render without manually loading the template
        return render(request, 'contact/contact_form.html', {'form': form})
    except TemplateDoesNotExist:
        # Handle the error if template is not found
        messages.error(request, "Template contact_form.html not found.")
        return redirect('contact_form')


def newsletter_subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')  # Get the email from the POST data

        # Check if the email is already subscribed
        if Newsletter.objects.filter(email=email).exists():
            messages.info(
                request, "You have already subscribed to this newsletter.")
        else:
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "You have successfully \
                        subscribed to the newsletter!")
            else:
                messages.error(
                    request, "Invalid email address. Please try again.")

    return redirect('home')
