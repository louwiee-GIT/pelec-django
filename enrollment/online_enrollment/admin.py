from django.contrib import admin
from .models import TestingDatabase,Student_info,Course,Enrollment,Payment,Schedule


admin.site.register(TestingDatabase)
admin.site.register(Student_info)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Payment)
admin.site.register(Schedule)

# Register your models here.

