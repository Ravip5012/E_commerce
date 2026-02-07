from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

import requests

from .import models
from .import serializer
import math


def index(request):
    products = models.ProductsOfWebShopi.objects.all()[:50]  
    return render(request, "index.html", {"products": products})

# shop/views.py
from django.shortcuts import render, get_object_or_404
from .models import ProductsOfWebShopi

def product(request, pk):
    # Fetch the product
    product = get_object_or_404(ProductsOfWebShopi, pk=pk)

    # --- handle recently viewed products session ---
    recently_viewed = request.session.get('recently_viewed', [])

    if pk in recently_viewed:
        recently_viewed.remove(pk)

    recently_viewed.insert(0, pk)
    recently_viewed = recently_viewed[:5]  # Keep only last 5 products

    request.session['recently_viewed'] = recently_viewed
    # -----------------------------------------------

    # Optional: fetch all products for “related products” section
    fetch_product = ProductsOfWebShopi.objects.all()

    context = {
        'product': product,
        'fetch_product': fetch_product
    }
    return render(request, "product.html", context)

    

# def load_products(request):
#     r = requests.get('https://dummyjson.com/products?limit=100')
#     # print(r.json())
#     for item in r.json():
#         product = models.ProductsOfWebShopi(
#             title=item['title'],
#             description=item['description'],
#             price=item['price'],
#             image_url=item['image']
#         )
#         product.save()

#     return render(request, 'index.html')





@login_required
def cart_view(request):
    """Show all cart items in template"""
    cart, created = models.Cart.objects.get_or_create(user=request.user)  # unpack
    
    cart_items = models.CartItem.objects.filter(cart=cart)  # now cart is correct
    cart_total = sum(item.total_price() for item in cart_items)

    context = {
        "cart_items": cart_items,
        "cart_total": cart_total,
    }
    return render(request, "cart.html", context)



@login_required
def add_to_cart(request, product_id):
    """Add product to cart (template version)"""
    product = get_object_or_404(models.ProductsOfWebShopi, id=product_id)
    cart, _ = models.Cart.objects.get_or_create(user=request.user)

    cart_item, created = models.CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")  


@login_required
def update_cart_item(request, item_id):
    """Update quantity from template form"""
    if request.method == "POST":
        cart_item = get_object_or_404(models.CartItem, id=item_id, cart__user=request.user)
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
    return redirect("cart")


@login_required
def remove_cart_item(request, item_id):
    """Remove an item from cart"""
    if request.method == "POST":
        cart_item = get_object_or_404(models.CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()
    return redirect("cart")



def search_products(request):
    query = request.GET.get('q', '')
    if query:
        product_data = models.ProductsOfWebShopi.objects.filter(title__icontains=query)
    else:
        product_data = models.ProductsOfWebShopi.objects.all()
    return render(request, 'index.html', {'product_data': product_data, 'query': query})



def search(request):
    query = request.GET.get('q', '')
    if query:
        filtered_products = models.ProductsOfWebShopiobjects.filter(title__icontains=query)
    else:
        filtered_products = models.ProductsOfWebShopi.objects.none()  # no results if empty query
    
    return render(request, 'search_result.html', {'products': filtered_products, 'query': query})


# def checkout(request):
#     return render(request, 'checkout.html',{})

def contact_page(request):
    return render(request, "contact.html")











