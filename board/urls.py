from django.urls import path

from board import views

urlpatterns = [
    path('list/', views.board_list)
]
