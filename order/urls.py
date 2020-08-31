from django.urls import path

from order.views import OrderCreate
from product.views import ProductList, ProductCreate, ProductDetail

urlpatterns = [
    # path('', ProductList.as_view()),
    # path('<int:pk>/', ProductDetail.as_view()),
    path('create/', OrderCreate.as_view()),
]
