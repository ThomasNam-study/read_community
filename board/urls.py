from django.urls import path

from board import views

urlpatterns = [
    path('list/', views.board_list, name='list'),
    path('detail/<int:pk>', views.board_detail, name='detail'),
    path('write/', views.board_write, name='write')
]
