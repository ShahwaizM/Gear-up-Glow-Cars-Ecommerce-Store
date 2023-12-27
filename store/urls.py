from django.contrib import admin
from django.urls import path
from .views.home import Index 
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.store import store
from .views.contact import  contact_page
from .views.about import About
from .views.ppolicy import ppolicy
# from .views.subscriber import subscribe
from .views.productdetail import ProductDetailView

urlpatterns = [
    path('', Index.as_view(), name='homepage'),

    path('store/', store.as_view() , name='store'),
    path('contact/', contact_page , name='contact_page'),
    # path('', subscribe , name='subscribe'),
    path('about/', About.as_view() , name='about'),
    path('privacypolicy/', ppolicy.as_view() , name='privacypolicy'),


    path('signup', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),

    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('cart/', auth_middleware(Cart.as_view()) , name='cart'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='productdetails'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]
