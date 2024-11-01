from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.projecthomepage, name='projecthomepage'),
     path('printpagecall/',views.printpagecall, name='printpagecall'),
     path('printpagelogic',views.printpagelogic,name='printpagelogic'),
     path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
     path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
     path('randompagecall/', views.randompagecall, name='randompagecall'),
     path('randomlogic/', views.randomlogic, name='randomlogic'),
     path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),
     path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
     path('add_task/', views.add_task, name='add_task'),
     path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('datetimeCall/', views.datetimeCall, name='datetimeCall'),
    path('datetimelogic/', views.datetimelogic, name='datetimelogic'),
     path('feedback_view/', views.feedback_view, name='feedback_view'),
     path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
     path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
     path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
     path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
     path('logout/', views.logout, name='logout'),
    path('add_student', views.add_student, name='add_student'),
    path('upload/', views.upload_file, name='uploadFileForm'),
    path('student_list',views.Student_list,name='Student_list'),
    path('facultyapp/', include(('facultyapp.urls', 'facultyapp'))),
    path('add/', views.add_contact, name='add_contact'),
    path('con/', views.contact_list, name='contact_list'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
path('student_list/', views.Student_list, name='student_list'),

]