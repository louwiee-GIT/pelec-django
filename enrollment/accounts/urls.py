from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registeruser, name='register_user'),
    path('login',views.LoginUSer, name='login'),
    path('logout/',views.Logout_user, name='logout_user'),
    path('dashboard/',views.dashboard, name='dashboard'),
]