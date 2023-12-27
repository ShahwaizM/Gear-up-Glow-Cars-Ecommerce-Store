from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from store.models.product import Products

class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        products = None

        products = Products.get_all_products()

        return render(request, 'productdetails.html', {
            'product': product,
            'products':products
        })

    def post(self , request,pk):
        product = get_object_or_404(Products, pk=pk)
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('productdetails',pk=pk)
