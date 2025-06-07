from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(EmployeeDT)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in EmployeeDT._meta.fields]      

from django.contrib import admin
from .models import EmployeeDT,product_need
        

@admin.register(product_need)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'product','site','qty','rate','amount','grand_total','timestamp','msg_status')
    search_fields = ('employee', 'product','site','qty','rate','amount','grand_total','timestamp','msg_status')        
    