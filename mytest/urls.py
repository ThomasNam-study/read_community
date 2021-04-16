from django.urls import path

from mytest import views

urlpatterns = [
    path('test', views.mytest),
]
