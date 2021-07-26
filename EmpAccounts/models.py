from typing import Callable
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from datetime import date

from django.db.models.fields.related import OneToOneField

gender_choices = [
    ('M','Male'),
    ('F','Female')
]
department = [
    ('Information Technology','IT'),
    ('Mobile App Development','MAD'),
    ('Java','Java'),
    ('Human Resources','HR'),
    ('Database Management','DBMS'),
    ('Admin','Admin'),
]
attendance_status = [
    ('Absent','Absent'),
    ('Present','Present')
]
#defining model for new employee to register
class EmpData(models.Model):
    Name = models.CharField(max_length=120, null=True, blank=False)
    Address = models.TextField(max_length=2000,null=True, blank=True)
    Email = models.CharField(max_length=120,null=True,blank=False)
    Phone = models.CharField(null=True,max_length=10)
    Gender = models.CharField(max_length=20,choices=gender_choices,default='Male')
    Department = models.CharField(max_length=40,null=True,choices=department,default='HR')
    ip_address = models.CharField(max_length=120,null=True,blank=True,)
    empID = models.CharField(max_length=120,blank=True,null=True)
    apporoved_Status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.Name)
    class Meta:
        verbose_name = "Employee Registration"

class ApprovedEmp(models.Model):
    employee = models.OneToOneField(EmpData, on_delete=CASCADE)
    loginID = models.CharField(max_length=120,null=True)
    password = models.CharField(max_length=120,null=True)
    def __str__(self):
        return self.employee.Name
    
    class Meta:
        verbose_name_plural="Approved Employees"


class WorkingDay(models.Model):
    dates = models.DateField(blank=False,unique=True)
    def __str__(self) -> str:
        return str(self.dates)

class AttendanceData(models.Model):
    employee = models.ForeignKey(ApprovedEmp,on_delete=CASCADE)
    date = models.ForeignKey(WorkingDay,on_delete=CASCADE)
    attendance = models.CharField(choices=attendance_status,max_length=120,null=True)
    active_Status = models.BooleanField(default=False)
    login_time = models.TimeField(null=True,blank=True)
    logout_time = models.TimeField(null=True,blank=True)
    def __str__(self) -> str:
        datestring = str(self.date)
        connectedString = datestring + '-'+ self.employee.employee.Name
        return str(connectedString)
    class Meta:
        verbose_name_plural = "Attendance Data"



class WorkDonePerDay(models.Model):
    task_assignment = models.TextField(null=True)
    attendance_date = models.ForeignKey(WorkingDay,on_delete=CASCADE,blank=True,null=True)
    employee = models.ForeignKey(ApprovedEmp,on_delete=CASCADE,blank=False,null=True)
    task_status = models.TextField(null=True,blank=True)
    task_completed = models.BooleanField(blank=True,null=True,default=False)
    def __str__(self) -> str:
        return str(self.attendance_date)+'-'+ self.employee.employee.Name
    class Meta:
        db_table = 'Tasks'
        verbose_name = 'Task'
    