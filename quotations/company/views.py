from django.shortcuts import render , HttpResponse , redirect
from .models import *
from django.contrib import messages
from employee.models import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == 'POST':
        print('post')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        print(email, password)
        try:
            company_dt = company_details.objects.get(email = email)
            print(company_dt, company_dt.company_id)
            # return redirect('deshboard')
            if password == company_dt.password: 
                if company_dt.status:
                    request.session['company_id'] = company_dt.company_id
                    return redirect('deshboard')
                else:
                    messages.error(request, 'User Not active')  
            else:
                messages.error(request, 'Wrong password')     
        except : 
            messages.error(request, 'User not find.') 
    return render(request , 'Company/login.html')


def logout(request):
    if 'company_id' in request.session:    
        del request.session['company_id']
    return redirect('cmp_login') 

from datetime import date, timedelta  

def Deshboard(request):
    if 'company_id' not in request.session:
        return redirect('cmp_login')  # Agar session me company_id nahi hai to login pe redirect kare

    company_id = request.session.get('company_id')
    company_dt = company_details.objects.get(company_id = company_id)  
    # employees = EmployeeDT.objects.filter(company=company_dt).count()

    
    # today = date.today()
    # current_year = today.year
    # current_month = today.month


    context = {
        # "monthly_report": monthly_report,
        # "yearly_report": yearly_report,
  
    }
   
    return render(request , 'Company/dashboard.html',context)

# ===========================================================================
from django.shortcuts import render, get_object_or_404, redirect
from .models import product
from .forms import ProductForm

def product_list(request):
    products = product.objects.all()
    return render(request, 'Company/list.html', {'products': products})

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'Company/form.html', {'form': form})

def product_update(request, pk):
    product_instance = get_object_or_404(product, pk=pk)
    form = ProductForm(request.POST or None, instance=product_instance)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'Company/form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'Company/confirm_delete.html', {'product': product})

# ===========================================================================
# Company/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Site
from .forms import SiteForm

def site_list(request):
    sites = Site.objects.all().order_by('-timestamp')
    return render(request, 'Company/site_list.html', {'sites': sites})

def site_create(request):
    form = SiteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('site_list')
    return render(request, 'Company/site_form.html', {'form': form})

def site_update(request, pk):
    site_instance = get_object_or_404(Site, pk=pk)
    form = SiteForm(request.POST or None, instance=site_instance)
    if form.is_valid():
        form.save()
        return redirect('site_list')
    return render(request, 'Company/site_form.html', {'form': form})

def site_delete(request, pk):
    site_instance = get_object_or_404(Site, pk=pk)
    if request.method == 'POST':
        site_instance.delete()
        return redirect('site_list')
    return render(request, 'Company/site_confirm_delete.html', {'site': site_instance})


#============================================================================
from django.shortcuts import render, get_object_or_404, redirect
from employee.models import EmployeeDT
from .forms import EmployeeForm

def employee_list(request):
    employees = EmployeeDT.objects.all()
    return render(request, 'Company/emp_list.html', {'employees': employees})

def employee_create(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'Company/emp_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(EmployeeDT, pk=pk)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'Company/emp_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(EmployeeDT, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'Company/emp_confirm_delete.html', {'employee': employee})


'''=============================== edit_company_details ======================================'''

from django.shortcuts import render, get_object_or_404, redirect
from .models import company_details
from .forms import CompanyDetailsForm

def edit_company_details(request):
    if 'company_id' not in request.session:
        return redirect('cmp_login')

    company_id = request.session.get('company_id')
    company_dt = company_details.objects.get(company_id = company_id)
    company = get_object_or_404(company_details, company_id=company_id)

    if request.method == "POST":
        form = CompanyDetailsForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('deshboard')  # Redirect to company list or detail page
    else:
        form = CompanyDetailsForm(instance=company)

    return render(request, 'Company/edit_company.html', {'form': form,'company_dt':company_dt})


# =========================================================================================

# ==================================================================
# views.py
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from employee.models import product_need, EmployeeDT
from company.models import Site, product
from django.template.loader import get_template
from xhtml2pdf import pisa
from decimal import Decimal
from django.utils.dateparse import parse_date
import datetime
from io import BytesIO

def product_need_list(request):
    needs = product_need.objects.all()
    return render(request, 'Company/product_need_list.html', {'needs': needs})

def product_need_create(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        site_id = request.POST.get('site')
        employee = EmployeeDT.objects.get(id=employee_id)
        site = Site.objects.get(id=site_id)
        grand_total = Decimal(0)
        for i in range(1, 11):
            pid = request.POST.get(f'product{i}')
            qty = request.POST.get(f'qty{i}')
            rate = request.POST.get(f'rate{i}')
            status = request.POST.get(f'msg_status{i}') == 'on'
            if pid and qty and rate:
                prod = product.objects.get(id=pid)
                qty = int(qty)
                rate = Decimal(rate)
                amount = qty * rate
                grand_total += amount
                product_need.objects.create(
                    employee=employee,
                    site=site,
                    product=prod,
                    qty=qty,
                    rate=rate,
                    amount=amount,
                    grand_total=grand_total,
                    msg_status=status
                )
        return redirect('product_need_list')
    employees = EmployeeDT.objects.all()
    sites = Site.objects.all()
    products = product.objects.all()
    return render(request, 'Company/product_need_create.html', {
        'employees': employees,
        'sites': sites,
        'products': products,
        'range': range(1, 11)
    })

def product_need_update(request, pk):
    need = get_object_or_404(product_need, pk=pk)
    if request.method == 'POST':
        form = productNeedForm(request.POST, instance=need)
        if form.is_valid():
            form.save()
            return redirect('product_need_list')
    else:
        form = productNeedForm(instance=need)
    return render(request, 'Company/product_need_update.html', {'form': form})

def product_need_delete(request, pk):
    need = get_object_or_404(product_need, pk=pk)
    if request.method == 'POST':
        need.delete()
        return redirect('product_need_list')
    return render(request, 'Company/product_need_delete.html', {'need': need})

def generate_invoice_filtered(request):
    employees = EmployeeDT.objects.all()
    sites = Site.objects.all()
    items = []
    total = 0
    employee = None
    site = None
    from_date = None
    to_date = None

    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        site_id = request.POST.get('site')
        from_date = parse_date(request.POST.get('from_date'))
        to_date = parse_date(request.POST.get('to_date'))

        if employee_id and site_id and from_date and to_date:
            employee = get_object_or_404(EmployeeDT, id=employee_id)
            site = get_object_or_404(Site, id=site_id)

            items = product_need.objects.filter(
                employee=employee,
                site=site,
                timestamp__date__range=(from_date, to_date)
            )
            total = sum(item.amount for item in items)

            template = get_template('Company/invoice_template_pdf.html')
            html = template.render({
                'employee': employee,
                'site': site,
                'items': items,
                'total': total,
                'date': datetime.date.today(),
                'invoice_no': f"A{employee_id}{site_id}{datetime.datetime.now().strftime('%d%m%Y')}"
            })
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
            pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=response)
            return response

    return render(request, 'Company/invoice_template.html', {
        'employees': employees,
        'sites': sites,
        'from_date': from_date,
        'to_date': to_date,
    })
