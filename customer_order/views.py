from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from dashboard.models import Product, Category, Order
from utils.group_list import Group_list


# Create your views here.



def Home_page(request):

    product_list = Product.objects.filter(is_active=True).order_by('-created_at')
    paginator = Paginator(product_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    object_list = Group_list(page_obj.object_list)
    category = Category.objects.filter(is_active=True)
    url = request.get_full_path()
    if url != '/':
        current_url = url.split('/category/')[1]
    else:
        current_url = '/'
    context = {
        'page_obj': page_obj,
        'product_list': object_list,
        'paginator': paginator,
        'categories':category,
        'current_url': current_url
    }
    return render(request , 'customer_order/home_page.html' , context)

def Category_view(request , category):
    product_list = Product.objects.filter(is_active=True , category__name=category)
    paginator = Paginator(product_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    object_list = Group_list(page_obj.object_list)
    category = Category.objects.filter(is_active=True)
    url = request.get_full_path()
    if url != '/':
        current_url = url.split('/category/')[1]
    else:
        current_url = '/'
    context = {
        'page_obj': page_obj,
        'product_list': object_list,
        'paginator': paginator,
        'categories':category,
        'current_url':current_url
    }
    return render(request , 'customer_order/home_page.html' , context)

def Login_page(request):
    return render(request , 'customer_order/login_page.html')



def Login_Process(request):
    if not request.user.is_authenticated:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username = username).first()
        if user is not None:
            check_pass = user.check_password(password)
            if check_pass:
                login(request , user)
                return JsonResponse({'status':'successful'})
        else:
            return JsonResponse({'status':'failed'})

    else:
        return redirect(reverse('home-page'))

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('login-page'))
    else:
        return redirect(reverse('login-page'))


def Register_page(request):
    return render(request , 'customer_order/register.html')


def Create_account(request):
    data = request.POST
    username = data.get('username')
    password = data.get('password')
    fullname = data.get('fullname')
    companyname = data.get('company_name')

    user = User.objects.filter(username=username).first()
    if user is not None:
        return JsonResponse({'status':'username already taken'})
    else:
        new_user = User(username=username , first_name=fullname , last_name=companyname)
        new_user.set_password(password)
        new_user.save()
        return JsonResponse({'status':'successful'})


def Order_Request(request):
    if request.user.is_authenticated:
        data = request.POST
        id = data.get('id')
        product = Product.objects.filter(id=id).first()
        if product is not None:
            quantity = data.get('quantity')
            if product.inventory_quantity is not None:
                if int(product.inventory_quantity) >= int(quantity):
                    Order.objects.create(user_id=request.user.id , product_id=id , quantity=quantity , status='Awaiting for Confirmation...')
                    return JsonResponse({'status':'successful'})
                else:
                    return JsonResponse({'status': 'no'})
            else:
                return JsonResponse({'status': 'no'})
        else:
            return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status':'redirect'})



def Myorders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user_id=request.user.id).order_by('status_2').order_by('-created_at')
        context = {
            'orders':orders
        }
        return render(request , 'customer_order/orders_page.html',context)
    else:
        return redirect(reverse('login-page'))