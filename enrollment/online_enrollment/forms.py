from django import forms
from .models import Student_info,Course

class Student_Form(forms.ModelForm):

    class Meta: 
        model = Student_info
        fields = '__all__'  
        

class Course_form(forms.ModelForm):

    class Meta: 
        model = Course
        fields = '__all__'    

