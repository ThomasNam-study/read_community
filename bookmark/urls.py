from django.urls import path

from bookmark.views import BookmarkLv, BookmarkDv

urlpatterns = [
    path('', BookmarkLv.as_view(), name='index'),
    path('<int:pk>', BookmarkDv.as_view(), name='detail'),
]
