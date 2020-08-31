from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, FormView, DetailView

from order.forms import OrderForm
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


class ProductDetail(DetailView):
    template_name = 'product_detail.html'

    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = OrderForm(self.request)

        return context
