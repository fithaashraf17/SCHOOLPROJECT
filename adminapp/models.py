
from sqlite3 import Date
from time import time

from django.db import models

# Create your models here.
class sessionyear_tb(models.Model):
    session_start_year=models.DateField()
   
    
    
    session_end_year=models.DateField()

class teacher_tb(models.Model):
    name=models.CharField(max_length=200,default="")
    photo=models.FileField(upload_to="tea")
    
    fathername=models.CharField(max_length=200,default="")
    mothername=models.CharField(max_length=200,default="")
    section= models.CharField(max_length=200,default="")
    dob=models.CharField(max_length=32,default='')
    phone=models.CharField(max_length=500,default='')
    qualification=models.CharField(max_length=500,default='')
    gender=models.CharField(max_length=500,default='')
    
    address=models.CharField(max_length=500,default='')
   
    experience=models.CharField(max_length=500,default='')
    subject=models.CharField(max_length=500,default='')
   
    email=models.CharField(max_length=200,default="")
    organisationaddress=models.CharField(max_length=200,default="")
    password=models.CharField(max_length=32,default='')
    designation=models.CharField(max_length=200,default="")
    achievments=models.CharField(max_length=32,default='')
    document=models.FileField(upload_to="teacher")



  
    status=models.CharField(max_length=200,default="pending")
    hpassword=models.TextField(default='')

class staff(models.Model):
    name=models.CharField(max_length=200,default="")
    photo=models.FileField(upload_to="tea")
    
    fathername=models.CharField(max_length=200,default="")
    mothername=models.CharField(max_length=200,default="")
    section= models.CharField(max_length=200,default="")
    dob=models.CharField(max_length=32,default='')
    phone=models.CharField(max_length=500,default='')
    
    gender=models.CharField(max_length=500,default='')
    
    address=models.CharField(max_length=500,default='')
   
    


  
    status=models.CharField(max_length=200,default="pending")


class course_tb(models.Model):
    coursename=models.CharField(max_length=200,default="")
class subject_tb(models.Model):
    subjectname=models.CharField(max_length=200,default="")
    teacherid=models.ForeignKey(teacher_tb,on_delete=models.CASCADE)
    courseid=models.ForeignKey(course_tb,on_delete=models.CASCADE)


class student_tb(models.Model):
   
    sesid=models.ForeignKey(sessionyear_tb,on_delete=models.CASCADE,null=True)
    photo=models.FileField(upload_to="student")
    courseid=models.ForeignKey(course_tb,on_delete=models.CASCADE,null=True)
    fathername=models.CharField(max_length=200,default="")
    mothername=models.CharField(max_length=200,default="")
    standard=models.CharField(max_length=200,default="")
    dob=models.CharField(max_length=32,default='')
    phone=models.CharField(max_length=500,default='')
    admission_no=models.CharField(max_length=500,default='')
    gender=models.CharField(max_length=500,default='')
    feetype=models.CharField(max_length=500,default='')
    address=models.CharField(max_length=500,default='')
    
    
    roll=models.CharField(max_length=500,default='')
    regno=models.CharField(max_length=500,default='')
    name=models.CharField(max_length=200,default="")
    # image=models.FileField(upload_to="user")
    email=models.CharField(max_length=200,default="")
   
    password=models.CharField(max_length=32,default='')
  

  
    status=models.CharField(max_length=200,default="pending")
    hpassword=models.TextField(default='')
    



class leave_report_student(models.Model):
   
    studentid=models.ForeignKey(student_tb,on_delete=models.CASCADE)
    leavedate=models.CharField(max_length=200,default="")
    leave_message=models.TextField()
    status=models.CharField(max_length=200,default="pending")

class leave_report_teacher(models.Model):
   
    teacherid=models.ForeignKey(teacher_tb,on_delete=models.CASCADE)
    leavedate=models.CharField(max_length=200,default="")
    leave_message=models.TextField()
    status=models.CharField(max_length=200,default="pending")

class feedback_stud(models.Model):
   
    studentid=models.ForeignKey(student_tb,on_delete=models.CASCADE)

    feedback=models.TextField()
    feedbackreply=models.TextField()
    

    
class feedback_teacher(models.Model):
   
    teacherid=models.ForeignKey(teacher_tb,on_delete=models.CASCADE)

    feedback=models.TextField()
    feedbackreply=models.TextField()
class notification_stud(models.Model):
   
    studentid=models.ForeignKey(student_tb,on_delete=models.CASCADE)

    message=models.TextField()
class notification_teacher(models.Model):
   
    teacherid=models.ForeignKey(student_tb,on_delete=models.CASCADE)

    message=models.TextField()
class fee_tb(models.Model):
    date=models.CharField(max_length=200,default="")
    studentid=models.ForeignKey(student_tb,on_delete=models.CASCADE, null=True)
    feetype=models.CharField(max_length=200,default="")
    feeamount=models.CharField(max_length=200,default="")
    clas=models.CharField(max_length=200,default="")
    status=models.CharField(max_length=200,default="pending")
    period=models.CharField(max_length=200,default="quarter1")
    
class attendance_student_tb(models.Model):
   
    studentid=models.ForeignKey(student_tb,on_delete=models.CASCADE)
    month=models.CharField(max_length=200,default="")

    
    total_lec=models.CharField(max_length=200,default="")

    lec_attended=models.CharField(max_length=200,default="")
    status=models.CharField(max_length=200,default="pending")

  

class timetable(models.Model):
    clas=models.CharField(max_length=200,default="")
    div=models.CharField(max_length=200,default="")
    day=models.CharField(max_length=200,default="")
    
    period1=models.CharField(max_length=200,default="")
    period2=models.CharField(max_length=200,default="")
    period3=models.CharField(max_length=200,default="")
    period4=models.CharField(max_length=200,default="")
    period5=models.CharField(max_length=200,default="")
class salary(models.Model):

    teacherid = models.ForeignKey(teacher_tb, on_delete=models.CASCADE,null=True)
    salarytype = models.CharField(max_length=200,default="")
    allowance =models.CharField(max_length=200,default="")
    month=models.CharField(max_length=200,default="")
    date=models.CharField(max_length=200,default="")
    status=models.CharField(max_length=200,default="pending")


class StudentResult(models.Model):

    studentid = models.ForeignKey(student_tb, on_delete=models.CASCADE)

    subject1 = models.FloatField(default=0)
    subject2 = models.FloatField(default=0)
    subject3 = models.FloatField(default=0)
    subject4 = models.FloatField(default=0)
    subject5 = models.FloatField(default=0)
    subject_assignment_marks = models.CharField(max_length=200,default="")
    sem=models.CharField(max_length=200,default="")

    examtype=models.CharField(max_length=200,default="")
    totalmark=models.CharField(max_length=200,default="")
    studentmark=models.CharField(max_length=200,default="")
    grade=models.CharField(max_length=200,default="")
    status=models.CharField(max_length=200,default="pending")

class contact(models.Model):

    fname=models.CharField(max_length=200,default="")
    lname=models.CharField(max_length=200,default="")
    email=models.CharField(max_length=200,default="")
    phone=models.CharField(max_length=200,default="")
    date=models.CharField(max_length=32,default='')
class notice(models.Model):
    date=models.CharField(max_length=200,default="")
  
    exam=models.CharField(max_length=200,default="")
    time=models.CharField(max_length=200,default="")
    standard=models.CharField(max_length=200,default="")
    status=models.CharField(max_length=200,default="pending")