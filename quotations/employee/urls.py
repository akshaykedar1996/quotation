from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('', Emp_login , name='emp_login'),
    path('log-out/', Emp_logout , name='emp_logout'),
    path('dashboard/', Emp_Dashboard , name='Emp_Dashboard'),
    
    # path('product-need/', product_need_list, name='product_need_list'),
    # path('product-need/add/', product_need_create, name='product_need_create'),
    # path('product-need/edit/<int:pk>/', product_need_update, name='product_need_update'),
    # path('product-need/delete/<int:pk>/', product_need_delete, name='product_need_delete'),

        path('product-need/add/', submit_multiple_entries, name='submit_multiple_entries'),
 
]
