import datetime

from django.shortcuts import render

# Create your views here.
def projecthomepage(request):
    return render(request,'adminapp/Projecthomepage.html')

def printpagecall(request):
    return render(request,'adminapp/printer1.html')

def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    a1= {'user_input':user_input}
    return render(request,'adminapp/printer1.html',a1)

def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num=int(user_input)
            result=10/num
        except Exception as e:
            error_message = str(e)
        return render(request,'adminapp/ExceptionExample.html', {'result' : result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')

import random
import string
def randompagecall(request):
    return render(request, 'adminapp/randomExample.html')
def randomlogic(request):
    if request.method=="POST":
        number1=int(request.POST['number1'])
        ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=number1))
    a1={'ran':ran}
    return render(request,'adminapp/randomExample.html',a1)

def calculatorpagecall(request):
    return render(request, 'adminapp/calculator.html')

def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, UploadFileForm
from .models import Task


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html', {'form': form, 'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

    return redirect('add_task')
import datetime

from django.shortcuts import render
import datetime

def datetimeCall(request):
    return render(request, 'adminapp/datetimeexample.html')

def datetimelogic(request):
    if request.method == "POST":
        try:
            number1 = int(request.POST['date1'])
            x = datetime.datetime.now()
            result = x + datetime.timedelta(days=number1)
            return render(request, 'adminapp/datetimeexample.html', {'result': result})
        except ValueError:
            error = "Invalid input. Please enter a valid integer."
            return render(request, 'adminapp/datetimeexample.html', {'error': error})
    return render(request, 'adminapp/datetimeexample.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegisterPage.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.shortcuts import render, redirect


def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPage.html')


def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if len(username) == 10:
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')
            elif len(username) == 4:
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')
            else:
                messages.error(request, 'Username length does not match student or faculty criteria.')
        else:
            messages.error(request, 'Invalid username or password.')

        return render(request, 'adminapp/UserLoginPage.html')

    return render(request, 'adminapp/UserLoginPage.html')


from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def logout(request):
    auth_logout(request)
    return redirect('projecthomepage')




#from .forms import StudentForm
#from .models import studentList

#def add_student(request):
 #   if request.method == 'POST':
#      form = StudentForm(request.POST)
 #       if form.is_valid():
  #          form.save()
   #         return redirect('student_list')
   # else:
    #    form = StudentForm()
    #return render(request, 'adminapp/add_student.html', {'form': form})

def Student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})



from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()
        monthly_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: monthly_names[x - 1])

        plt.figure(figsize=(10, 6))  # Add a figure size for better visualization
        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%')
        plt.title('Sales Distribution per Month')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')  # Use correct encoding

        return render(request, 'adminapp/chart.html', {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'chart': image_data
        })

    return render(request, 'adminapp/chart.html', {'form': UploadFileForm()})


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback

from django.shortcuts import render
from .forms import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            form = FeedbackForm()  # Reset form after submission
    else:
        form = FeedbackForm()

    return render(request, 'adminapp/feedback_view.html', {'form': form})

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'adminapp/add_student.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# View for listing and searching contacts
def contact_list(request):
    query = request.GET.get('query')
    if query:
        contacts = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(email__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'adminapp/contact_list.html', {'contacts': contacts})

# View for adding a new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            if request.POST.get('email_recipient'):
                send_mail(
                    subject=f'New Contact: {contact.name}',
                    message=f'Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\nAddress: {contact.address}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[request.POST['email_recipient']],
                )
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'adminapp/add_contact.html', {'form': form})

# View for deleting a contact
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'adminapp/delete_contact.html', {'contact': contact})
