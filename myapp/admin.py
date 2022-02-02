from django.contrib import admin
from adminapp.models import *

# Register your models here.

admin.site.register(student_tb)
admin.site.register(teacher_tb)
admin.site.register(sessionyear_tb)