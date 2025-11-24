from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.students , name = 'students' ),
    path('students_info/', views.students_info , name = 'students_info' )

]
