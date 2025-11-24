from django.shortcuts import render,redirect,get_object_or_404
from .forms import Student_Form,Course_form
from .models import Student_info,Course,Enrollment,Payment,Schedule


def studentinfo_view(request):
    students = Student_info.objects.all().values()
    return render(request,'student_info.html',{'students':students})



def cours_view(request):
   courses = Course.objects.all().values()
   return render(request,'course.html',{'courses':courses})



def enrollment_views(request):
   enrollments = Enrollment.objects.all().values()
   return render(request,'enrollments.html',{'enrollments':enrollments})



def payment_views(request):
   payments = Payment.objects.all().values()
   return render(request,'payments.html',{'payments': payments})



def schedule_views(request):
   schedules = Schedule.objects.all().values()
   return render(request,'schedules.html',{'schedules': schedules})


def add_stud(request):
   if request.method == 'POST':
      form = Student_Form(request.POST)
      if form.is_valid():
         form.save()
         return redirect('add_students')
      
   else: 
      form = Student_Form()
   return render(request,'add_stud.html',{'form':form})

def edit_stud(request, pk):
   student = get_object_or_404(Student_info,pk=pk)
   if request.method == 'POST':
      form = Student_Form(request.POST,instance=student)
      if form.is_valid():
         form.save()
         return redirect('add_students')
      
   else: 
      form = Student_Form()
   return render(request,'edit_stud.html',{'form':form})

def add_course(request):
   if request.method == 'POST':
      form = Course_form(request.POST)
      if form.is_valid():
         form.save()
         return redirect('add_course')
      
   else: 
      form = Course_form()
   return render(request,'add_course.html',{'form':form})

def edit_course(request,pk):
   course = get_object_or_404(Course,pk=pk)
   if request.method == 'POST':
      form = Course_form(request.POST,instance=course)
      if form.is_valid():
         form.save()
         return redirect('add_course')
      
   else: 
      form = Course_form()
   return render(request,'edit_course.html',{'form':form})
