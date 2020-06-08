from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from bookmark.models import Bookmark


class BookmarkLv(ListView):
    model = Bookmark


class BookmarkDv(DetailView):
    model = Bookmark
