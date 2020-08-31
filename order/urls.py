from django.urls import path

from order.views import OrderCreate, OrderList
from product.views import ProductList, ProductCreate, ProductDetail

urlpatterns = [
    path('', OrderList.as_view()),
    path('create/', OrderCreate.as_view()),
]
