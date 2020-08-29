from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, FormView

from product.forms import RegisterForm
from product.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product.html'

class ProductCreate(FormView):
    model = Product
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'