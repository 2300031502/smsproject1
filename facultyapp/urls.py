from django.urls import path
from . import views

app_name = 'facultyapp'

urlpatterns = [
    path('', views.FacultyHomePage, name='FacultyHomePage'),
    path('add_content/', views.add_content, name='add_content'),
    path('add_course/', views.add_course, name='add_course'),
    path('view_student_list/', views.view_student_list, name='view_student_list'),
    path('logout/', views.logout, name='logout'),
    path('delete_content/<int:pk>/', views.delete_content, name='delete_content'),
    path('post_marks/', views.post_marks, name='post_marks'),
]
