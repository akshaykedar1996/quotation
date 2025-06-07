from django.db import models
from company.models import company_details,product,Site
# Create your models here.
# Model to represent a day off
class DayOff(models.Model):
    date = models.DateField()
    employee_code = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')


# Model to represent an extra off day
class ExtraOff(models.Model):
    date = models.DateField()
    employee_code = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')
       
import uuid       
class EmployeeDT(models.Model):
    employee_code = models.CharField(max_length=8, unique=True, blank=True, default=uuid.uuid4().hex[:8])
    company = models.ForeignKey(company_details, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)  # New field for activation status

    SHIFT_CHOICES = [
        ('Day Shift', 'Day Shift'),
        ('Night Shift', 'Night Shift'),
        
    ]

    Work_sift = models.CharField(
        max_length=90, 
        choices=SHIFT_CHOICES, 
        blank=True, 
        null=True
    )
    

    Employ_check_id = models.CharField(max_length=50, blank=True, null=True)
    check_st = models.CharField(max_length=50, blank=True, null=True)
    verify_image = models.ImageField(upload_to='atendanc/', blank=True, null=True)

    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=50,blank=True, null=True)
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    verify_code = models.CharField(max_length=15,blank=True, null=True)
############################ Personal_dt page ###############################################
   # image = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)

    Date_of_Birth = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    Gender = models.CharField(max_length=50, blank=True, null=True)
    Blood_Group = models.CharField(max_length=50, blank=True, null=True)
    Marital_Status= models.CharField(max_length=50, blank=True, null=True)
    Marriage_Anniversary = models.DateField(verbose_name="Marriage Anniversary", blank=True, null=True)
    Personal_Email = models.EmailField(blank=True, null=True)
    Alternate_Phone_Number = models.CharField(max_length=15,blank=True, null=True)

    Current_Address = models.CharField(max_length=500,blank=True, null=True)
    Permanent_Address = models.CharField(max_length=500,blank=True, null=True)
    House_Type = models.CharField(max_length=100,blank=True, null=True)
    Staying_at_Current_Residence_Since = models.CharField(max_length=100,blank=True, null=True)
    Living_in_Current_City_Since = models.CharField(max_length=100,blank=True, null=True)
################# wark page ##########################################
    
    Date_of_Joining = models.DateField(verbose_name="Date of Joining", blank=True, null=True)
    Basic_Salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Basic Salary
    Overtime_Rate = models.DecimalField(max_digits=5, decimal_places=2, default=50.00, blank=True, null=True)  # Per Hour Overtime Rate
    Work_hours = models.IntegerField(blank=True, null=True)
    PF_Percentage = models.DecimalField(max_digits=5, decimal_places=2, default=12.00, blank=True, null=True)  # PF Percentage
    TDS_Percentage = models.DecimalField(max_digits=5, decimal_places=2, default=10.00, blank=True, null=True)  # Tax Percentage

    
    Probation_Period = models.CharField(max_length=100,blank=True, null=True)
    Employee_Type = models.CharField(max_length=100,blank=True, null=True)
    Work_Location = models.CharField(max_length=300,blank=True, null=True)
    Employee_Status = models.CharField(max_length=100,blank=True, null=True)
    Work_Experience = models.CharField(max_length=100,blank=True, null=True)

    Designation = models.CharField(max_length=200,blank=True, null=True)
    Job_Title = models.CharField(max_length=200,blank=True, null=True)
    Department = models.CharField(max_length=200,blank=True, null=True)
    Sub_Department = models.CharField(max_length=200,blank=True, null=True)

    WORK_HISTORY = models.CharField(max_length=500,blank=True, null=True)

    Resignation_Date = models.CharField(max_length=500,blank=True, null=True)
    Resignation_Status = models.CharField(max_length=500,blank=True, null=True)
    Notice_Period = models.CharField(max_length=500,blank=True, null=True)
    Last_Working_Day = models.CharField(max_length=500,blank=True, null=True)

################# team page ##########################################  
    team_Name = models.CharField(max_length=500,blank=True, null=True)
    team_type = models.CharField(max_length=500,blank=True, null=True)
    team_Department = models.CharField(max_length=500,blank=True, null=True)
    team_Designation = models.CharField(max_length=500,blank=True, null=True)
################# EDUCATIONAL_INFO page ########################################## 
    EDUCATIONAL_INFO = models.CharField(max_length=500,blank=True, null=True)

################# FAMILY_INFO page ##########################################     
    Family_Name = models.CharField(max_length=200,blank=True, null=True)
    Family_Relationship  = models.CharField(max_length=200,blank=True, null=True)
    Family_Phone_Number  = models.CharField(max_length=200,blank=True, null=True)

      # ManyToManyFields for work week and extra off
    work_week = models.ManyToManyField(DayOff, blank=True)
    extra_off = models.ManyToManyField(ExtraOff, blank=True)

    def __str__(self):
      return self.name if self.name else f"Employee {self.id}"
       

from django.db import models
from employee.models import EmployeeDT
from company.models import product,Site

class product_need(models.Model):
    employee = models.ForeignKey(EmployeeDT, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1)  # ✅ lowercase + default
    qty = models.PositiveIntegerField(blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    msg_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} - {self.product}"

    

    
