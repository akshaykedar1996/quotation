from django.contrib import admin
from django.urls import path , include
from .views import *


urlpatterns = [

    path('', login , name='cmp_login'),
    path('logout/', logout , name='cmp_logout'),
    path('deshboard/', Deshboard , name='deshboard'),

    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/edit/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
    
    path('employees/', employee_list, name='employee_list'),
    path('employees/create/', employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', employee_delete, name='employee_delete'),
    
    path('product-need/', product_need_list, name='product_need_list'),
    path('product-need/create/', product_need_create, name='product_need_create'),
    path('product-need/update/<int:pk>/', product_need_update, name='product_need_update'),
    path('product-need/delete/<int:pk>/', product_need_delete, name='product_need_delete'),
    path('generate-invoice-filtered/', generate_invoice_filtered, name='generate_invoice_filtered'), # ✅ new
    
    path('sites/', site_list, name='site_list'),
    path('sites/add/', site_create, name='site_create'),
    path('sites/<int:pk>/edit/', site_update, name='site_update'),
    path('sites/<int:pk>/delete/', site_delete, name='site_delete'),
    
    path('edit-company/', edit_company_details, name='edit_company'),
]
