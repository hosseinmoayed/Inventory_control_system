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
    path('' , views.dashboard_view , name='dashboard-index'),
    path('products-dashboard/' , views.product_view , name='dashboard-product'),
    path('products-dashboard/<type>' , views.product_view , name='add-product'),
    path('orders-dashboard/' , views.order_view , name='dashboard-orders'),
    path('customer-order-dashboard/' , views.customer_order , name='dashboard-customer_order'),
    path('application-status/<id>/<status>' , views.Application_status , name='application-status'),
]
