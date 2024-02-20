

from django.urls import path
from django.contrib.auth.views  import LoginView
from . import views

urlpatterns = [
    path('login/',LoginView.as_view() ,name = 'login'),
    path('logout/', views.logout_view, name='logout'),
]