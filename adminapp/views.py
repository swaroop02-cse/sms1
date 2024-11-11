from django.contrib.auth import authenticate, login, logout
from django.db import models
from .forms import StudentForm
from .models import StudentList
class SportEvent(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    sport_type = models.CharField(max_length=50, choices=[('basketball', 'Basketball'), ('cricket', 'Cricket'), ('football', 'Football')])

    def __str__(self):
        return self.name
import datetime
import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime as dt
import calendar

from .models import Task
from .forms import TaskForm

def projecthomepage(request):
    return render(request, 'adminapp/HomePage.html')


def printpagecall(request):
    return render(request, 'adminapp/print.html')


def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        print(f'User input: {user_input}')
        a1 = {'user_input': user_input}
        return render(request, 'adminapp/print.html', a1)
    return render(request, 'adminapp/print.html')


def randomlogic(request):
    if request.method == "POST":
        try:
            number1 = int(request.POST.get('number1', 0))
            ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
            a1 = {'ran': ran}
            return render(request, 'adminapp/random.html', a1)
        except ValueError:
            a1 = {'ran': 'Invalid input'}
            return render(request, 'adminapp/random.html', a1)
    return render(request, 'adminapp/random.html')


def randompagecall(request):
    return render(request, 'adminapp/random.html')


def exceptionpagecall(request):
    return render(request, 'adminapp/Exception.html')


def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/Exception.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/Exception.html')


def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation', '')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Infinity'
            else:
                result = 'Invalid operation'
        except ValueError as e:
            result = str(e)
        return render(request, 'adminapp/calculator.html', {'result': result})
    return render(request, 'adminapp/calculator.html')


def calculatorpage(request):
    return render(request, 'adminapp/calculator.html')


def datetimepagelogic(request):
    if request.method == "POST":
        try:
            number1 = int(request.POST.get('date',0))

            x = dt.now()
            ran = x + datetime.timedelta(days=number1)
            ran1 = ran.year
            ran2 = calendar.isleap(ran1)
            ran3 = "Leap Year" if ran2 else "Not Leap Year"
            a1 = {'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
            return render(request, 'adminapp/datetime.html', a1)
        except ValueError as e:
            return render(request, 'adminapp/datetime.html', {'error': str(e)})
    return render(request, 'adminapp/datetime.html')


def datetimepage(request):
    return render(request, 'adminapp/datetime.html')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request,'adminapp/add_task.html',{'form': form,'tasks': tasks})
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/register.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/HomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')


def UserLoginPageCall(request):
    return render(request, 'adminapp/login.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:studenthomepage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:facultyhomepage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    else:
        return render(request, 'adminapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminapp/student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})
