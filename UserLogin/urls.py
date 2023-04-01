from django.urls import path
from UserLogin import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login

#Crearemos las urls para nuestro Login-Logout.

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', logout_then_login, name='Logout'),
]
