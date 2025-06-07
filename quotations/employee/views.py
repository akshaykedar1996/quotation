from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , HttpResponse , redirect

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib import messages
from datetime import datetime
from datetime import date, timedelta    

@csrf_exempt
def Emp_login(request):
    if request.method == 'POST':
        print('post')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        try:
            Employee_dt = EmployeeDT.objects.get(email = email)
            # return redirect('deshboard')
            if password == Employee_dt.password: 
                if Employee_dt.is_active:
                    request.session['employee_id'] = Employee_dt.employee_code
                    return redirect('Emp_Dashboard')
                else:
                    messages.error(request, 'User Not active')  
            else:
                messages.error(request, 'Wrong password')     
        except : 
            messages.error(request, 'User not find.') 
    return render(request,'Employee/login.html')

def Emp_logout(request):
    if 'employee_id' in request.session:    
        del request.session['employee_id']
    return redirect('emp_login') 


from django.shortcuts import render

def Emp_Dashboard(request):
    return render(request, 'Employee/dashboard.html')


# ===============================================================================
from django.shortcuts import render, redirect
from .models import product_need, product, EmployeeDT
from company.models import Site
from decimal import Decimal
from django.contrib import messages

def submit_multiple_entries(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        site_id = request.POST.get('site')

        if not employee_id or not site_id:
            messages.error(request, "Please select both employee and site.")
            return redirect('submit_multiple_entries')

        try:
            employee = EmployeeDT.objects.get(id=employee_id)
        except EmployeeDT.DoesNotExist:
            messages.error(request, "Employee not found.")
            return redirect('submit_multiple_entries')

        try:
            site = Site.objects.get(id=site_id)
        except Site.DoesNotExist:
            messages.error(request, "Site not found.")
            return redirect('submit_multiple_entries')

        grand_total = Decimal(0)
        has_data = False

        for i in range(1, 11):
            prod_id = request.POST.get(f'product{i}')
            qty = request.POST.get(f'qty{i}')
            rate = request.POST.get(f'rate{i}')
            msg_status = request.POST.get(f'msg_status{i}') == 'on'

            if prod_id and qty and rate:
                try:
                    qty = int(qty)
                    rate = Decimal(rate)
                    amount = qty * rate
                    grand_total += amount

                    product_obj = product.objects.get(id=prod_id)

                    product_need.objects.create(
                        employee=employee,
                        product=product_obj,
                        site=site,
                        qty=qty,
                        rate=rate,
                        amount=amount,
                        grand_total=grand_total,
                        msg_status=msg_status
                    )
                    has_data = True
                except Exception as e:
                    messages.error(request, f"Error in row {i}: {e}")

        if has_data:
            messages.success(request, "Products submitted successfully.")
        else:
            messages.warning(request, "No valid product rows submitted.")

        return redirect('submit_multiple_entries')

    employees = EmployeeDT.objects.all()
    products = product.objects.all()
    sites = Site.objects.all()
    return render(request, 'Employee/product_need_form.html', {
        'employees': employees,
        'products': products,
        'sites': sites,
        'range': range(1, 11)
    })


def cancel_submission(request):
    return redirect('/')


def success_view(request):
    entries = product_need.objects.all()
    return render(request, 'success.html', {'entries': entries})