"""
URL configuration for inventory_control project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.Home_page , name='home-page'),
    path('login/' , views.Login_page , name='login-page'),
    path('register/' , views.Register_page , name='register-page'),
    path('login_process/' , views.Login_Process , name='login_process'),
    path('logout/' , views.Logout , name='logout'),
    path('create_account/' , views.Create_account , name='create-account'),
    path('category/<category>' , views.Category_view , name='category'),
    path('order_request/' , views.Order_Request , name='order-request'),
    path('myorders/' , views.Myorders, name='my-orders'),
]
