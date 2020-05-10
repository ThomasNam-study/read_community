from django.urls import path

from fcuser import views

urlpatterns = [
    path('register/', views.register),
]
