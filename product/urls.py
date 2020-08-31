from django.urls import path

from product.views import ProductList, ProductCreate, ProductDetail

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>/', ProductDetail.as_view()),
    path('create/', ProductCreate.as_view()),
]
