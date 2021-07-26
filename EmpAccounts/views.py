from .models import *
from django.contrib.auth import authenticate
from django.http.response import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .utils import *
import json
import logging
from datetime import date,datetime


logging.basicConfig(filename='userdata.logs',level=logging.INFO,format='%(asctime)s %(message)s')
logging.basicConfig(filename='Erros.logs',level=logging.WARNING,format='%(asctime)s %(message)s')

def home_page(request):
    return render(request, 'home-page.html',{})


def registration_page(request):
    form = EmpForms()
    ip=get_ip()
    if request.method == 'POST':
        form = EmpForms(request.POST)
        if form.is_valid():
            new_join = form.save(commit=False)
            new_join.ip_address = get_ip()
            logging.info(f'{new_join.Name} just registered!')
            form.save()
            return render(request,'successpage.html')

        else:
            logging.warning('user was not created due to wrong info')
            messages.error(request,'not created')
            print(form.errors)
        
    return render(request,'registration.html',{'form':form,'ip':ip})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                logging.info(f'Admin {user.username} just logged in')
                
            else:
                try:
                    emp = ApprovedEmp.objects.get(loginID=username)
                    date_today = WorkingDay.objects.get(dates=date.today())
                    current_time = datetime.now().strftime("%H:%M")
                    print('marking attendance')      
                    attendance_mark = AttendanceData.objects.create(employee=emp,date=date_today)  
                    #AttendanceData.objects.update(employee=emp,login_time=current_time)
                    attendance_mark.login_time = current_time
                    attendance_mark.save()
                    print(attendance_mark)                                            
                    login(request,user)
                except:
                    login(request,user)
                    logging.info(f'{user.username} just logged in')
            return redirect("dashboard-page")
        else:
            print('not verified')
    return render(request,'login.html',{})

def logout_page(request):
    try:
        if request.user.is_superuser:
            logout(request)
            logging.info(f'Admin {request.user} just logged out')

        else:
            current_time = datetime.now().strftime("%H:%M")
            emp = ApprovedEmp.objects.get(loginID=request.user.username)
            date_today = WorkingDay.objects.get(dates=date.today())
            atten=AttendanceData.objects.get(employee=emp,date=date_today)
            atten.logout_time=current_time
            atten.attendance = 'Present'
            atten.save()
            logging.info(f'{request.user} just logged out')
            logout(request)
    except:
        logout(request)
        print('there was an error')
    return redirect('login-page')
#def apporoval_of_employee(request):

@login_required(login_url='login-page')
def dashboard_view(request):
    empObj = EmpData.objects.all()
    current_date = date.today()
    try:
        workinday = WorkingDay.objects.get(dates=current_date)
        attendance_of_emp = AttendanceData.objects.filter(date=workinday)
    except:
        attendance_of_emp = []
    if request.user.is_superuser:
        return render(request,'admin-panel/dashboard.html',{'employees':empObj,'attendances':attendance_of_emp})
    else:        
        employee= ApprovedEmp.objects.get(loginID = request.user)               #normal user dashboard
        return render(request,'user-panel/dashboard.html',{'employee':employee})

def pending_approvals(request):
    if request.user.is_superuser:
        emp = EmpData.objects.all()
        return render(request,'admin-panel/approvals.html',{'emp':emp})
    else:
        return HttpResponse('<h1>You are not authorized to visit this page</h1>') 

def employees_data_view(request):
    emp= ApprovedEmp.objects.all()
    admin = ['Human Resources','Admin']
    return render(request,'admin-panel/employeesdata.html',{'emp':emp,'hr':admin})



def approve_emp(request):
    data = json.loads(request.body)
    action = data['action']
    empid = data['empid']
    #checking if approved button is called
    if action =='approve':
        emp = EmpData.objects.get(id=empid)
        #approving employee
        emp.apporoved_Status = True
        #generating id and password
        emp.empID = generate_id()
        user_id = username_generator(emp.Name)
        user_password = password_generator()
        name= emp.Name.partition(" ")
        first_name = name[0]
        last_name = name[1]
        admins = ['Human Resources','Admin']
        #checking if employee is of HR department
        if emp.Department in admins:
            print(emp.Department)
            user = User.objects.create_superuser(username = user_id,
            password = user_password,
            first_name = first_name,
            last_name = last_name,
            email = emp.Email)
            user.save()
        #creating user for login
        else:
            user = User.objects.create_user(
            username = user_id,
            password = user_password,
            first_name = first_name,
            last_name = last_name,
            email = emp.Email) 
            user.save()
        #to send id password to mail 
        send_email(user_id, user_password,userEmail=emp.Email)
        emp.save()
        ApprovedEmp.objects.create(employee=emp,loginID=user_id,password=user_password) 
        return JsonResponse('this employee was approved',safe=False)

def emp_application_view(request,id):
    emp = ApprovedEmp.objects.get(id=id)
    return render(request,'admin-panel/employeeProfile.html',{'emp':emp})

def calender_view(request):
    return render(request,'admin-panel/calender.html')

def attendance_data_view(request):
    dates = WorkingDay.objects.all()
    return render(request,'admin-panel/attendanceData/attendanceData.html',{'dates':dates})

def employee_attendance_view(request):
    employee=ApprovedEmp.objects.all()
    return render(request,'admin-panel/attendanceData/eattendanceData.html',{'employees':employee})


def per_date_view(request,date):
    empty = 1

    try:
        date_now = WorkingDay.objects.get(dates=date)
        attendances = AttendanceData.objects.filter(date=date_now)
        if attendances.exists():
            empty=0
    except:
        attendances=[]
        messages.error(request,'this date donot exists')

    context ={'attendance':attendances,}
    return render(request,'admin-panel/attendanceData/perDate.html',context)


def per_emp_attendance_view(request,empID):
    if request.user.is_superuser:
        employee = ApprovedEmp.objects.get(id=empID)
        attendance = AttendanceData.objects.filter(employee=employee)
        return render(request,'admin-panel/attendanceData/peremployee.html',{'attendances':attendance,'emp':employee})
    else:
        employee = ApprovedEmp.objects.get(loginID=request.user)
        attendance = AttendanceData.objects.filter(employee=employee)
        return render(request,'user-panel/attendancedata.html',{'attendances':attendance,'emp':employee})


def about_view(request):
    return render(request,'aboutpage.html')

def qna_view(request):
    return render(request,'qnapage.html')

def assign_tasks(request):
    if request.user.is_superuser:
        try:
            today = date.today()
            current_date = WorkingDay.objects.get(dates=today)
            form = WorkDoneForm()
            if request.method =='POST':
                try:
                    form = WorkDoneForm(request.POST)
                    if form.is_valid:
                        new_form = form.save(commit=False)
                        new_form.attendance_date = current_date
                        form.save()
                        return redirect('tasks-status-page')
                except:
                    pass
            return render(request,'admin-panel/assignTask.html',{'form':form})
        except:
            return render(request,'admin-panel/assignTask.html',)
    else:
        return HttpResponse('<h1> You are not athourized to view this page</h1>')

def tasks_report(request):
    try:
        today = WorkingDay.objects.get(dates= date.today())
        task = WorkDonePerDay.objects.filter(attendance_date=today)
        context={
            'tasks':task
        }
    except:
        context={}
    return render(request,'admin-panel/taskStatus.html',context)


def check_your_tasks(request):
    try:
        employee = ApprovedEmp.objects.get(loginID=request.user)
        tasks = WorkDonePerDay.objects.filter(employee=employee)
        if request.method == 'POST':
            for task in tasks:
                task.task_status = request.POST['report']
                task.task_completed = True
                task.save()
            return redirect('mytasks')
    except:
        tasks = []
    return render(request,'user-panel/yourtasks.html',{'tasks':tasks})

def complain_view(request):
    return render(request,'complaintBox.html')


#test 2
def test_second(request):
    if request.method=='POST':
        emp = ApprovedEmp.objects.get(loginID=request.user.username)
        date_today = WorkingDay.objects.get(dates=date.today())
        current_time = datetime.now().strftime("%H:%M")
        print('marking attendance')
        if request.user.is_superuser:
            print('super user entry')
        attendance_mark = AttendanceData.objects.create(employee=emp,date=date_today,attendance='Present',login_time=current_time)
        attendance_mark.save()
    attendance_mark=None
    return render(request,'test2.html',{'atten':attendance_mark})

def test_page(request):
    employee = ApprovedEmp.objects.get(loginID="Jelwin@26")
    emp = AttendanceData.objects.get(employee=employee)
   
    return render(request,'test.html',{'emp':emp,})