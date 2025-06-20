# Generated by Django 5.2 on 2025-06-04 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employee_code', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employee_code', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_code', models.CharField(blank=True, default='aab39c4c', max_length=8, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('Work_sift', models.CharField(blank=True, choices=[('Day Shift', 'Day Shift'), ('Night Shift', 'Night Shift')], max_length=90, null=True)),
                ('Employ_check_id', models.CharField(blank=True, max_length=50, null=True)),
                ('check_st', models.CharField(blank=True, max_length=50, null=True)),
                ('verify_image', models.ImageField(blank=True, null=True, upload_to='atendanc/')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('verify_code', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('Date_of_Birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('Gender', models.CharField(blank=True, max_length=50, null=True)),
                ('Blood_Group', models.CharField(blank=True, max_length=50, null=True)),
                ('Marital_Status', models.CharField(blank=True, max_length=50, null=True)),
                ('Marriage_Anniversary', models.DateField(blank=True, null=True, verbose_name='Marriage Anniversary')),
                ('Personal_Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Alternate_Phone_Number', models.CharField(blank=True, max_length=15, null=True)),
                ('Current_Address', models.CharField(blank=True, max_length=500, null=True)),
                ('Permanent_Address', models.CharField(blank=True, max_length=500, null=True)),
                ('House_Type', models.CharField(blank=True, max_length=100, null=True)),
                ('Staying_at_Current_Residence_Since', models.CharField(blank=True, max_length=100, null=True)),
                ('Living_in_Current_City_Since', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_of_Joining', models.DateField(blank=True, null=True, verbose_name='Date of Joining')),
                ('Basic_Salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Overtime_Rate', models.DecimalField(blank=True, decimal_places=2, default=50.0, max_digits=5, null=True)),
                ('Work_hours', models.IntegerField(blank=True, null=True)),
                ('PF_Percentage', models.DecimalField(blank=True, decimal_places=2, default=12.0, max_digits=5, null=True)),
                ('TDS_Percentage', models.DecimalField(blank=True, decimal_places=2, default=10.0, max_digits=5, null=True)),
                ('Probation_Period', models.CharField(blank=True, max_length=100, null=True)),
                ('Employee_Type', models.CharField(blank=True, max_length=100, null=True)),
                ('Work_Location', models.CharField(blank=True, max_length=300, null=True)),
                ('Employee_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('Work_Experience', models.CharField(blank=True, max_length=100, null=True)),
                ('Designation', models.CharField(blank=True, max_length=200, null=True)),
                ('Job_Title', models.CharField(blank=True, max_length=200, null=True)),
                ('Department', models.CharField(blank=True, max_length=200, null=True)),
                ('Sub_Department', models.CharField(blank=True, max_length=200, null=True)),
                ('WORK_HISTORY', models.CharField(blank=True, max_length=500, null=True)),
                ('Resignation_Date', models.CharField(blank=True, max_length=500, null=True)),
                ('Resignation_Status', models.CharField(blank=True, max_length=500, null=True)),
                ('Notice_Period', models.CharField(blank=True, max_length=500, null=True)),
                ('Last_Working_Day', models.CharField(blank=True, max_length=500, null=True)),
                ('team_Name', models.CharField(blank=True, max_length=500, null=True)),
                ('team_type', models.CharField(blank=True, max_length=500, null=True)),
                ('team_Department', models.CharField(blank=True, max_length=500, null=True)),
                ('team_Designation', models.CharField(blank=True, max_length=500, null=True)),
                ('EDUCATIONAL_INFO', models.CharField(blank=True, max_length=500, null=True)),
                ('Family_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Family_Relationship', models.CharField(blank=True, max_length=200, null=True)),
                ('Family_Phone_Number', models.CharField(blank=True, max_length=200, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company_details')),
                ('work_week', models.ManyToManyField(blank=True, to='employee.dayoff')),
                ('extra_off', models.ManyToManyField(blank=True, to='employee.extraoff')),
            ],
        ),
        migrations.CreateModel(
            name='product_need',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.CharField(blank=True, max_length=50, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('msg_status', models.BooleanField(blank=True, default=False, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeedt')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.product')),
            ],
        ),
    ]
