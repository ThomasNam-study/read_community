from django.urls import path

from product.views import ProductList, ProductCreate, ProductDetail, ProductListApi, ProductDetailApi

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>/', ProductDetail.as_view()),
    path('create/', ProductCreate.as_view()),

    path("api/", ProductListApi.as_view()),
    path("api/<int:pk>", ProductDetailApi.as_view()),
]
