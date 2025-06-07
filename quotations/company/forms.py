from django import forms
from .models import product

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name']
        
# Company/forms.py

from django import forms
from .models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Site Name'}),
        }
        


from django import forms
from employee.models import EmployeeDT

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeDT
        fields = '__all__'  # Sabhi fields include karna
        exclude = ['work_week', 'extra_off', 'Employ_check_id', 'check_st', 'password']  # Removed 'company'
        widgets = {
            'employee_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Employee Code'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # 'Work_sift': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Work Shift'}),
             'Work_sift': forms.Select(attrs={'class': 'form-control'}),
            'Work_hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Work Hours'}),
            'Employ_check_id': forms.TextInput(attrs={'class': 'form-control'}),
            'check_st': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            # 'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'verify_code': forms.TextInput(attrs={'class': 'form-control'}),

            # Personal Details
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'Date_of_Birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
            'Blood_Group': forms.TextInput(attrs={'class': 'form-control'}),
            'Marital_Status': forms.Select(attrs={'class': 'form-control'}, choices=[('Single', 'Single'), ('Married', 'Married')]),
            'Marriage_Anniversary': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Personal_Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Alternate_Phone_Number': forms.TextInput(attrs={'class': 'form-control'}),

            # Address Details
            'Current_Address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'Permanent_Address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'House_Type': forms.TextInput(attrs={'class': 'form-control'}),
            'Staying_at_Current_Residence_Since': forms.TextInput(attrs={'class': 'form-control'}),
            'Living_in_Current_City_Since': forms.TextInput(attrs={'class': 'form-control'}),

            # Work Details
            'Date_of_Joining': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Probation_Period': forms.TextInput(attrs={'class': 'form-control'}),
            'Employee_Type': forms.TextInput(attrs={'class': 'form-control'}),
            'Work_Location': forms.TextInput(attrs={'class': 'form-control'}),
            'Employee_Status': forms.TextInput(attrs={'class': 'form-control'}),
            'Work_Experience': forms.TextInput(attrs={'class': 'form-control'}),

            'Designation': forms.TextInput(attrs={'class': 'form-control'}),
            'Job_Title': forms.TextInput(attrs={'class': 'form-control'}),
            'Department': forms.TextInput(attrs={'class': 'form-control'}),
            'Sub_Department': forms.TextInput(attrs={'class': 'form-control'}),

            'WORK_HISTORY': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'Resignation_Date': forms.TextInput(attrs={'class': 'form-control'}),
            'Resignation_Status': forms.TextInput(attrs={'class': 'form-control'}),
            'Notice_Period': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_Working_Day': forms.TextInput(attrs={'class': 'form-control'}),

            # Team Details
            'team_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'team_type': forms.TextInput(attrs={'class': 'form-control'}),
            'team_Department': forms.TextInput(attrs={'class': 'form-control'}),
            'team_Designation': forms.TextInput(attrs={'class': 'form-control'}),

            # Educational Info
            'EDUCATIONAL_INFO': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

            # Family Info
            'Family_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Family_Relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'Family_Phone_Number': forms.TextInput(attrs={'class': 'form-control'}),

            # ManyToMany Fields
            'work_week': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'extra_off': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        


from django import forms
from .models import company_details

class CompanyDetailsForm(forms.ModelForm):
    class Meta:
        model = company_details
        fields = '__all__'  # Ya specific fields ['email', 'password', 'contact_no', 'Company_logo', ...]
        exclude = ['password']

        widgets = {
            'password': forms.PasswordInput(),
            'Company_logo': forms.ClearableFileInput(),
        }        