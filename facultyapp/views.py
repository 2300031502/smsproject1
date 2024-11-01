from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Blog

def FacultyHomePage(request):
    return render(request, 'facultyapp/FacultyHomePage.html')

def add_content(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:add_content')  # Use namespaced URL
    else:
        form = TaskForm()

    tasks = Blog.objects.all()
    return render(request, 'facultyapp/add_content.html', {'form': form, 'tasks': tasks})

def delete_content(request, pk):
    task = get_object_or_404(Blog, pk=pk)
    task.delete()
    return redirect('facultyapp:add_content')  # Use namespaced URL

from .forms import AddCourseForm
def add_course(request):
    if request.method=='POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:FacultyHomePage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/add_course.html', {'form':form})

from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
def logout(request):
    auth_logout(request)
    return redirect('projecthomepage')

from .models import AddCourse
from adminapp.models import StudentList
from django.contrib.auth.decorators import login_required


def view_student_list(request):
    print("view_student_list was called")  # Confirm function call
    course = request.GET.get('course')
    section = request.GET.get('section')

    print(f"Course: {course}, Section: {section}")  # Check GET parameters

    student_courses = AddCourse.objects.all()

    if course:
        student_courses = student_courses.filter(course=course)
        print(f"Filtered student_courses by course: {list(student_courses.values())}")  # Debugging
    if section:
        student_courses = student_courses.filter(section=section)
        print(f"Filtered student_courses by section: {list(student_courses.values())}")  # Debugging

    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    print(f"Students found: {list(students.values())}")  # Debugging

    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES

    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }

    print("Rendering the student list template")  # Confirm rendering
    return render(request, 'facultyapp/view_student_list.html', context)

from django.core.mail import send_mail
from django.contrib.auth.models import User  # Assuming User is your custom user model
from .models import StudentList
from .forms import  MarksForm




def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the student in the form
            student = marks_instance.student
            student_user = student.user

            if student_user and student_user.email:  # Check if student_user exists and has an email
                user_email = student_user.email
                subject = 'Marks Entered'
                message = f'Hello, {student_user.first_name}, marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
                from_email = 'venkatanagabalaji124@gmail.com'
                recipient_list = [user_email]
                send_mail(subject, message, from_email, recipient_list)
            else:
                # Handle cases where the user or email is missing
                print("User or email not found for student:", student)

            return render(request, 'facultyapp/marks_success.html')
    else:
        form = MarksForm()
    return render(request, 'facultyapp/post_marks.html', {'form': form})
