from django.urls import path
from . import views


urlpatterns = [
    path('registrations/', views.registration , name = 'registrations' ),
    path('newstudent_registration/', views.newstudent_registration , name = 'newstudent_registration' )
]
