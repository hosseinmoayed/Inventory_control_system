from apscheduler.triggers.cron import CronTrigger
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from dashboard.models import Category, Product, Rop, Inventory, News, Order
from utils.calc import eoq , rop
import datetime
from datetime import timedelta
# Create your views here.
from apscheduler.schedulers.background import BackgroundScheduler


def my_job():
    order_del = Rop.objects.filter(status=False).all()
    if order_del:
        date_today = datetime.date.today()
        for order in order_del:
            order_date = order.order_delivery_time
            if date_today == order_date:
                order.status = True
                order.save()
                text = order.product.name
                News.objects.create(text=f'{text} Was received!')
    return True


scheduler = BackgroundScheduler()
scheduler.add_job(
    my_job,
    trigger=CronTrigger(hour='*/23'),  # Every 23 hour
    id="my_job",  # The `id` assigned to each job MUST be unique
    max_instances=1,
    replace_existing=True,
)
scheduler.start()

@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def dashboard_view(request):

    products = Product.objects.filter(is_active=True).prefetch_related('inventory_set')


    context = {
        'product_list':products,

    }
    return render(request , 'dashboard/dashboard.html' , context=context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def product_view(request , type=''):
    category = Category.objects.filter(is_active=True)
    data = request.POST
    if type == 'add':
        category_check = Category.objects.filter(name=data.get('category')).first()
        if category_check is not None:
            image = request.FILES.get('productphoto')
            price = data.get('price')
            D = float(data.get('D'))
            A = float(data.get('A'))
            h = float(data.get('h'))
            L = float(data.get('L'))
            result_eoq = eoq(h=h, A=A, D=D)
            result_rop = rop(eoq=result_eoq, D=float(D), L=float(L))
            new_product = Product.objects.create(
                category_id=category_check.id,
                name=data.get('name'),
                demand=D,
                holding_cost=h,
                ordering_cost=A,
                order_delivery_time=L,
                eoq=result_eoq,
                rop=result_rop,
                price=price,
                image=image,
                seller_company=data.get('company_name'),
            )
            today_date = datetime.date.today()
            order_del = L*365
            delivery_date = today_date + timedelta(days=order_del)
            Rop.objects.create(product_id=new_product.id , company_name=data.get('company_name') , quantity=result_eoq , order_delivery_time=delivery_date )



            return redirect(reverse('dashboard-product'))

    products = Product.objects.filter(is_active=True).order_by('created_at').prefetch_related('inventory_set')
    orders = Order.objects.filter(status_2=True , status='Confirmed')
    context = {
        'categories':category,
        'products':products,
        'orders':orders
    }

    return render(request , 'dashboard/product.html' , context=context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def order_view(request):
    order_list = Rop.objects.all().order_by('status')
    context = {
        'orders':order_list
    }
    return render(request , 'dashboard/order.html' , context=context)



@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def customer_order(request):
    orders = Order.objects.all().order_by('status_2').order_by('status_2').order_by('-created_at').prefetch_related('product__inventory_set')
    context = {
        'orders':orders
    }
    return render(request, 'dashboard/customer_order.html' , context)



@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def Application_status(request , id , status):
    order_n = Order.objects.filter(id=id).first()
    if order_n is not None and order_n.status_2==False:
        if status == 'accept':
            order_n.status='Confirmed'
            order_n.status_2 = True
            order_n.save()
            order_n.product.inventory_quantity = order_n.product.inventory_quantity - order_n.quantity
            order_n.product.save()
            if order_n.product.inventory_quantity <= order_n.product.rop:
                today_date = datetime.date.today()
                order_del = order_n.product.order_delivery_time * 365
                delivery_date = today_date + timedelta(days=order_del)
                print(order_n.product.seller_company)
                Rop.objects.create(product_id=order_n.product.id, company_name=order_n.product.seller_company,
                                   quantity=order_n.product.eoq, order_delivery_time=delivery_date)
        else:
            order_n.status = 'Declined'
            order_n.status_2 = True
            order_n.save()
    return redirect(reverse('dashboard-customer_order'))


def topside(request):
    news = News.objects.order_by('-created_at').first()
    context = {
        'news':news
    }
    return render(request , 'dashboard/includes/topside.html' , context)


