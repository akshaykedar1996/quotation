from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
@admin.register(company_details)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in company_details._meta.fields]   

        

@admin.register(Invoice)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in Invoice._meta.fields]          



@admin.register(Client)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in Client._meta.fields]      

  

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')
    search_fields = ('name', 'timestamp')    