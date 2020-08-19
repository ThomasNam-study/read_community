from django.urls import path

from fcuser import views
from fcuser.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
]
