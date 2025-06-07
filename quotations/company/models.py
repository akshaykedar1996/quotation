from django.db import models
import uuid   # Unique ID ke liye

# Create your models here.
class company_details(models.Model):

    company_id = models.CharField(max_length=8, unique=True, blank=True, default=uuid.uuid4().hex[:8])
    email = models.EmailField(unique=True)  
    password = models.CharField(max_length=12)  
    contact_no = models.CharField(max_length=15, unique=True)
    verification_code = models.CharField(max_length=6, blank=True, null=True) 
    is_verified = models.BooleanField(default=False)  
    status = models.BooleanField(default=False) 
    Attendance_camera = models.BooleanField(default=False,blank=True,null=True)
    
    Company_logo = models.ImageField(upload_to='company/logos/', blank=True,null=True)
    Company_address = models.TextField(blank=True, null=True)  # Address

    Registered_Company_Name = models.CharField(max_length=100,blank=True, null=True)
    Brand_Name = models.CharField(max_length=100,blank=True, null=True)
    Company_Official_Email = models.EmailField(blank=True, null=True)
    Company_Official_Contact = models.CharField(max_length=15,blank=True, null=True)
    Website = models.CharField(max_length=50,blank=True, null=True)
    Domain_Name = models.CharField(max_length=50,blank=True, null=True)
    Industry_Type = models.CharField(max_length=100,blank=True, null=True)
    REGISTERED_OFFICE_add = models.CharField(max_length=500,blank=True, null=True)
    CORPORATE_OFFICE_add = models.CharField(max_length=500,blank=True, null=True)
    CUSTOM_ADDRESS_TITLE_add = models.CharField(max_length=500,blank=True, null=True)

    LIVE_ANNOUNCEMENTS = models.CharField(max_length=1000,blank=True, null=True)
    COMPANY_POLICIES = models.CharField(max_length=2000,blank=True, null=True)

    

    # ROLE_CHOICES = (
    #     ('admin', 'Admin'),
    #     ('hr', 'HR Manager'),
    #     ('inventory', 'Inventory Manager'),
    #     ('sales', 'Sales Manager'),
    #     ('finance', 'Finance Manager'),
    # )
    # role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.Registered_Company_Name if self.Registered_Company_Name else "Unnamed Company"



class Attendance_Status(models.Model):
    last_run_date = models.DateField(null=True, blank=True)    



from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# ✅ Expense Model - Yeh company ke kharche ko store karega
class Expense(models.Model):
    company = models.ForeignKey(company_details, on_delete=models.CASCADE)
    Employee_ID = models.CharField(max_length=100,blank=True, null=True)
    CATEGORY_CHOICES = [
        ('Salary', 'Salary'),
        ('Office Supplies', 'Office Supplies'),
        ('Utilities', 'Utilities'),
        ('Marketing', 'Marketing'),
        ('Travel', 'Travel'),
    ]
    title = models.CharField(max_length=255)  # Expense ka naam
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Expense category
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount
    date = models.DateField(default=now)  # Expense date
    description = models.TextField(blank=True, null=True)  # Additional details

    def __str__(self):
        return self.title

# ✅ Invoice Model - Yeh client ko diye gaye bills ko store karega

from django.db import models
from django.utils.timezone import now

from django.db import models

class Client(models.Model):
    client_id = models.CharField(max_length=8, unique=True, blank=True, default=uuid.uuid4().hex[:8])
    company = models.ForeignKey(company_details, on_delete=models.CASCADE)
    Employee_ID = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255)  # Client ka naam
    email = models.EmailField(unique=True)  # Client ka email (Unique)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Phone number
    address = models.TextField(blank=True, null=True)  # Address
    gst_number = models.CharField(max_length=15, blank=True, null=True)  # GST Number (Optional)
    pan_number = models.CharField(max_length=10, blank=True, null=True)  # PAN Number (Optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Client creation date


    # ✅ Bank Details
    bank_name = models.CharField(max_length=255, blank=True, null=True)  # Bank ka naam
    account_number = models.CharField(max_length=20, blank=True, null=True, unique=True)  # Account Number
    ifsc_code = models.CharField(max_length=11, blank=True, null=True)  # IFSC Code
    account_type = models.CharField(max_length=10, choices=[('Saving', 'Saving'), ('Current', 'Current')], blank=True, null=True)  # Account Type

    def __str__(self):
        return self.name  # Client ka naam return karega



class Invoice(models.Model):
    company = models.ForeignKey(company_details, on_delete=models.CASCADE)
    Employee_ID = models.CharField(max_length=100, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,blank=True, null=True)  # ✔️ Ye sahi hai

    invoice_number = models.CharField(max_length=20, unique=True, blank=True, null=True)  # ✅ Unique Invoice Number
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Base Amount (Without Tax)
    due_date = models.DateField()  # Payment due date
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')  # Payment status
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0)  # GST percentage
    tds_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0)  # TDS percentage
    gst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)  # Auto Calculated
    tds_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)  # Auto Calculated
    total_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)  # Auto Calculated
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)  # Auto Calculated
    created_at = models.DateTimeField(auto_now_add=True)  # Invoice creation date

    def save(self, *args, **kwargs):
        self.amount = float(self.amount)  # Ensure amount is float
        self.gst_percentage = float(self.gst_percentage) if self.gst_percentage else 0
        self.tds_percentage = float(self.tds_percentage) if self.tds_percentage else 0

        self.gst_amount = (self.amount * self.gst_percentage) / 100
        self.tds_amount = (self.amount * self.tds_percentage) / 100
        self.total_tax = self.gst_amount + self.tds_amount
        self.grand_total = self.amount + self.gst_amount - self.tds_amount

        super().save(*args, **kwargs)

        # ✅ Jab Invoice Paid ho, to ek Credit Transaction create ho
        if self.status == "Paid":
            BankTransaction.objects.create(
                company=self.company,
                client=self.client,  # ✅ Client Assign
                transaction_type="Credit",
                amount=self.grand_total,
                date=now(),
                description=f"Invoice Payment Received: {self.invoice_number} {self.client.name} - ₹{self.grand_total}"
            )

    def __str__(self):
        return f"Invoice {self.client} - ₹{self.grand_total}"


class BankTransaction(models.Model):
    company = models.ForeignKey(company_details, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)  # ✅ Client Link
    Employee_ID = models.CharField(max_length=100, blank=True, null=True)
    transaction_type = models.CharField(max_length=20, choices=[('Credit', 'Credit'), ('Debit', 'Debit')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=now)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.client.name} - {self.transaction_type} - ₹{self.amount}"


# ✅ Profit & Loss Report Model - Yeh reports generate karega
class ProfitLoss(models.Model):
    company = models.ForeignKey(company_details, on_delete=models.CASCADE)
    Employee_ID = models.CharField(max_length=100,blank=True, null=True)
    month = models.CharField(max_length=50)
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    expenses = models.DecimalField(max_digits=12, decimal_places=2)
    net_profit = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.month} - Profit: {self.net_profit}"
    
    

from django.db import models

class product(models.Model): 
    name = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    

class Site(models.Model): 
    name = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"    

   
    
