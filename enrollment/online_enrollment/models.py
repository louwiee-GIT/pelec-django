from django.db import models

# Create your models here.


class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.first_name}'
    
class Student_info(models.Model):
    student_id = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    section = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.student_id} | {self.firstname} {self.lastname}'

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    course_format = models.CharField(max_length=100)
    units = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.course_name} | {self.course_code} | {self.course_format}'


class Enrollment(models.Model):
    enrollment_id = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    enrollment_date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
 

class Payment(models.Model):

    payment_id = models.CharField(max_length=100)
    enrollment_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    payment_date = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.payment_id} | {self.amount} | {self.payment_date} | {self.payment_status}'



class Schedule(models.Model):

    schedule_id = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    days = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    room = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.schedule_id} | {self.course_id} | {self.days} | {self.time} | {self.room}'






