from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)





class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/product', null=True, blank=True)
    price = models.IntegerField(null=True)
    inventory_quantity = models.IntegerField(null=True)
    demand = models.IntegerField()
    holding_cost = models.FloatField()
    ordering_cost = models.FloatField()
    order_delivery_time = models.FloatField()
    eoq = models.IntegerField(null=True , blank=True)
    rop = models.IntegerField(null=True , blank=True)
    seller_company = models.CharField(max_length=100 , null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return str(self.name)



class ZeroProduct(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Inventory(models.Model):
    product = models.ForeignKey(to=Product , on_delete=models.CASCADE , null=True)
    zero = models.OneToOneField(to=ZeroProduct , on_delete=models.CASCADE , null=True)
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)




class Rop(models.Model):
    product = models.ForeignKey(to=Product , on_delete=models.CASCADE , related_name='+')
    order_delivery_time = models.DateField(null=True)
    quantity = models.IntegerField(null=True)
    company_name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.name} --> {self.company_name}'

    def save(self, *args, **kwargs):
        if self.status == True:
            zero = ZeroProduct.objects.create(quantity=0)
            Inventory.objects.create(quantity=self.quantity, product_id=self.product.id,zero_id=zero.id)
            self.product.inventory_quantity = self.quantity
            self.product.save()
        return super(Rop, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product , on_delete=models.CASCADE , related_name='+')
    quantity = models.IntegerField()
    status = models.CharField(max_length=30 , null=True)
    status_2 = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.last_name)



class News(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)




