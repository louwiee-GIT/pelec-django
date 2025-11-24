from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.courses, name = 'courses' ),
    path('shift_course/', views.shift_course, name = 'shift_course' )
]
