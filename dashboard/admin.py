from django.contrib import admin

# Register your models here.
from . import models
from .models import Inventory, Product , ZeroProduct



class RopAdmin(admin.ModelAdmin):
    def save_model(self, request, obj: models.Rop, form, change):
        if change:
            if obj.status == True:
                zero=ZeroProduct.objects.create(quantity=0)
                Inventory.objects.create(quantity=obj.quantity, product_id=obj.product.id,zero_id=zero.id, status=True)
                obj.product.inventory_quantity = obj.quantity
                obj.product.save()
        super(RopAdmin, self).save_model(request, obj, form, change)



admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Rop)
admin.site.register(models.Order)
admin.site.register(models.News)
admin.site.register(models.ZeroProduct)
admin.site.register(models.Inventory)
