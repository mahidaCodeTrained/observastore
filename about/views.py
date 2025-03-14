from django.shortcuts import render
from .models import AboutPage

# Create your views here.


def about(request):
    """
    This will create a view that I can then use to showcase this backend data
    to the frontend using a template..
    """
    about = AboutPage.objects.first()
    if not about:
        about = None

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
