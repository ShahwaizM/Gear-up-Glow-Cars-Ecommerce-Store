from django.shortcuts import render , redirect
from django.http import HttpResponse

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

class Cart(View):
    def get(self, request):
        cart = request.session.get('cart', {})  # Use get with a default value to avoid None
        if cart:
            ids = list(cart.keys())
            products = Products.get_products_by_id(ids)
            print(products)
        else:
            products = []  # Define an empty list when the cart is empty

        return render(request, 'cart.html', {'products': products})
