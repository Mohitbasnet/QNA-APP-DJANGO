

from django.urls import path
from django.contrib.auth.views  import LoginView,PasswordChangeView,PasswordChangeDoneView
from . import views

urlpatterns = [
    path('login/',LoginView.as_view() ,name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/',PasswordChangeView.as_view(), name = 'password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name = 'password_change_done'),
]