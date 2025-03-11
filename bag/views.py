from django.shortcuts import render

# Create your views here.


def view_shopping_bag(request):
    return render(request, 'bag/shopping_bag.html')
