from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.projecthomepage, name = 'projecthomepage'),
    path('printpagecall/',views.printpagecall, name = 'printpagecall'),
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall, name = 'exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic, name = 'exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('calculatorpage/', views.calculatorpage, name='calculatorpage'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('datetimepage/', views.datetimepage, name='datetimepage'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('user_login/',views.UserLoginLogic,name='userloginpage'),
    path('userloginpagecall/',views.UserLoginPageCall,name='userloginpagecall'),
    path('logout/', views.logout, name='logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name = 'student_list'),
]