from django.urls import path

from product.views import ProductList, ProductCreate

urlpatterns = [
    path('', ProductList.as_view()),
    path('create/', ProductCreate.as_view()),
]
