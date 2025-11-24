from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentinfo_view, name='student'),
    path('courses/', views.cours_view, name='courses'),
    path('enrollments/', views.enrollment_views, name='enrollments'),
    path('payments/', views.payment_views, name='payments'),
    path('schedules/', views.schedule_views, name='schedules'),
    path('add_students/',views.add_stud,name='add_students'),
    path('edit_students/<int:pk>/',views.edit_stud,name='edit_students'),
    path('add_course/',views.add_stud,name='add_course'),
    path('edit_course/<int:pk>/',views.edit_stud,name='edit_course')
    
]
