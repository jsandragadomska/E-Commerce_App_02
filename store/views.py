from django.shortcuts import render
from .models import *

def store(request):
    ordering = ['-id']
    products = Product.objects.all
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def about(request):
    return render(request, 'store/about.html')

def blog(request):
    posts = Post.objects.all
    context = {'posts':posts}
    return render(request, 'store/blog.html', context)
