
from time import time
from unicodedata import name
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from adminapp.models import *
import os

import random
import string
from django.conf import settings
from django.core.mail import send_mail
import hashlib
import datetime




def adminindex(request):
    return render(request,"adminindex.html")
def inputs(request):
    return render(request,"input.html")

# def register(request):
#     if request.method == "POST":
#         cname = request.POST["name"]

#         cmail = request.POST["email"]
#         cpass = request.POST["password"]
    
#         cconfirm=request.POST["confirm password"]
#         cusertype = request.POST["user"]

#         hashpass = hashlib.md5(cpass.encode('utf8')).hexdigest()

#         check = reg_tb.objects.filter(email=cmail)
#         if check:
#             return render(request, "adminindex.html", {"msg": "same user exist"})
#         else:
#             if cpass == cconfirm:
#                 x = ''.join(random.choices(cname+string.digits, k=8))
#                 y = ''.join(random.choices(
#                     string.ascii_letters+string.digits, k=7))
#                 subject = "welcome to success path "
#                 message = f'hii{cname},thaks for registering,your email{cmail} and password is {cpass}'
#                 email_from = settings.EMAIL_HOST_USER
#                 recipient_list = [cmail, ]
#                 send_mail(subject, message, email_from, recipient_list)

#                 add = reg_tb(name=cname, email=cmail, user_type=cusertype, password=cpass, hpassword=hashpass)
#                 add.save()
#                 return render(request, "adminindex.html", {'msg': "user added"})
#             else:
#                 return render(request, "adminindex.html", {"msg": "password doesnt match"})
#     else:
#         return render(request, "adminindex.html")

def managestudent(request):
  
    query1=student_tb.objects.all()
      
    


    return render(request,"managestudent.html",{"reg":query1,})
def status(request):
    ii=request.GET['id']
    query=student_tb.objects.filter(id=ii).update(status='approved')
    query1=student_tb.objects.filter(status='pending')
    return  render(request,'adminindex.html',{"reg":query1})
    
def student_admission(request):
    q=sessionyear_tb.objects.all()

    c=course_tb.objects.all()
  
    if request.method == 'POST':

        cname = request.POST["name"]

        cmail = request.POST["email"]
        cpass = request.POST["password"]
    
        cconfirm=request.POST["confirmpassword"]
    
        
        cimg = request.FILES["image"]
        cdob = request.POST["dob"]
        cfee = request.POST["fee"]
        caddress = request.POST["address"]
        cgen= request.POST["gender"]
        cfname = request.POST["fname"]
        cmname = request.POST["mname"]
        cphone = request.POST["phone"]
        cclass = request.POST["class"]
        ccourse= request.POST["course"]
        admission = request.POST["admission"]
        croll = request.POST["roll"]
        creg = request.POST["regno"]
        ii = request.POST.get('ses')
        cid=request.POST.get('course')
        course=course_tb.objects.get(id=cid)
  
        ses =sessionyear_tb.objects.get(id=ii)
        
        hashpass = hashlib.md5(cpass.encode('utf8')).hexdigest()


        
        check = student_tb.objects.filter(regno=creg)
        if check:
            return render(request, "studentadmission.html", {"msg": "student  exist"})
        else:
            if cpass == cconfirm:
                x = ''.join(random.choices(cname+string.digits, k=8))
                y = ''.join(random.choices(
                    string.ascii_letters+string.digits, k=7))
                subject = "welcome to success path "
                message = f'hii{cname},thanks for registering,your email :{cmail} and password is {cpass}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [cmail, ]
                send_mail(subject, message, email_from, recipient_list)


                add = student_tb(sesid=ses,courseid=course,regno=creg,name=cname,hpassword=hashpass,email=cmail,password=cpass,photo=cimg,dob=cdob,feetype=cfee,address=caddress,gender=cgen,fathername=cfname,mothername=cmname,phone=cphone,standard=cclass,admission_no=admission,roll=croll)
        
                add.save()
                return render(request, "adminindex.html")
    else:

        return render(request, "studentadmission.html",{"reg":q,"courses":c})


def editstudent(request):
    ii = request.GET['id']
    query = student_tb.objects.filter(id=ii)
    q=sessionyear_tb.objects.all()
    q1=course_tb.objects.all()
    return render(request, "updatestudent.html", {'usr': query,'q':q,"q1":q1})
def updatestudent(request):
    if request.method == "POST":
        up = request.GET['id']
        cname = request.POST["name"]

        cmail = request.POST["email"]
        # cpass = request.POST["password"]
    
    
        
       
        cdob = request.POST["dob"]
        cfee = request.POST["fee"]
        caddress = request.POST["address"]
        cgen= request.POST["gender"]
        cfname = request.POST["fname"]
        cmname = request.POST["mname"]
        cphone = request.POST["phone"]
        cclass = request.POST["class"]
    
        cadmission = request.POST["admission"]
        croll = request.POST["roll"]
        creg = request.POST["regno"]
        ii = request.POST.get('ses')
        cid=request.POST.get('course')
        course=course_tb.objects.get(id=cid)
  
        ses =sessionyear_tb.objects.get(id=ii)
        
        

        imgup = request.POST["imgupdate"]
        print(imgup, "***********")
        if imgup == "Yes":
            image1 = request.FILES['image']
            oldrec = student_tb.objects.all().filter(id=up)
            uprec = student_tb.objects.get(id=up)
            for x in oldrec:
                imgurl = x.photo.url
                pathtoimage = os.path.dirname(
                    os.path.dirname(os.path.abspath(__file__)))+imgurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print("successfully removed")
            uprec.photo = image1
            uprec.save()
        student_tb.objects.filter(id=up).update(sesid=ses,courseid=course,regno=creg,name=cname,email=cmail,dob=cdob,feetype=cfee,address=caddress,gender=cgen,fathername=cfname,mothername=cmname,phone=cphone,standard=cclass,admission_no=cadmission,roll=croll)
        return render(request, "adminindex.html")
    else:
         return render(request, "adminindex.html")


def deletestudent(request):
    ii = request.GET['id']
    query = student_tb.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/myadmin/')
def deletestudentfee(request):
    ii = request.GET['id']
    fee_tb.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/myadmin/')
def teacherregistration(request):


    if request.method == 'POST':

        cname = request.POST["name"]

        cmail = request.POST["email"]
        cpass = request.POST["password"]
    
        cconfirm=request.POST["confirmpassword"]
    
        
        cimg = request.FILES["image"]
        cdob = request.POST["dob"]
       
        caddress = request.POST["address"]
        cgen= request.POST["gender"]
        cfname = request.POST["fname"]
        cmname = request.POST["mname"]
        cphone = request.POST["phone"]
        cqualification = request.POST["qualification"]
       
        cexp = request.POST["experience"]
        csub = request.POST["subject"]
        corg= request.POST["organisation"]
        cdes= request.POST["designation"]
        cach= request.POST["achievments"]
        cdoc = request.FILES["doc"]
        se=request.POST['section']
     
        
        
        hashpass = hashlib.md5(cpass.encode('utf8')).hexdigest()


        
        check = teacher_tb.objects.filter(email=cmail)
        if check:
            return render(request, "teacherreg.html", {"msg": "teacher  exist"})
        else:
            if cpass == cconfirm:
                x = ''.join(random.choices(cname+string.digits, k=8))
                y = ''.join(random.choices(
                    string.ascii_letters+string.digits, k=7))
                subject = "welcome to success path "
                message = f'hii{cname},thanks for registering,your email :{cmail} and password is {cpass}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [cmail, ]
                send_mail(subject, message, email_from, recipient_list)


                add = teacher_tb(section=se,name=cname,hpassword=hashpass,email=cmail,password=cpass,photo=cimg,dob=cdob,qualification=cqualification,experience=cexp,subject=csub,organisationaddress=corg,designation=cdes,achievments=cach,document=cdoc, address=caddress,gender=cgen,fathername=cfname,mothername=cmname,phone=cphone)
                add.save()
                return render(request, "adminindex.html")
    else:

        return render(request, "teacherreg.html")
    

def manageteacher(request):
  
    query1=teacher_tb.objects.all()
      
    


    return render(request,"manageteacher.html",{"reg":query1,})


def statustea(request):
    ii=request.GET['id']
    query=teacher_tb.objects.filter(id=ii).update(status='approved')
    query1=teacher_tb.objects.filter(status='pending')
    return  render(request,'adminindex.html',{"reg":query1})
def updateteacher(request):
    up = request.GET['id']



    if request.method == 'POST':

        cname = request.POST["name"]

        cmail = request.POST["email"]
        cpass = request.POST["password"]
    
        
    
        
     
        cdob = request.POST["dob"]
        # clan = request.POST["language"]
        caddress = request.POST["address"]
        cgen= request.POST["gender"]
        cfname = request.POST["fname"]
        cmname = request.POST["mname"]
        cphone = request.POST["phone"]
        cqualification = request.POST["qualification"]
        
        cexp = request.POST["experience"]
        csub = request.POST["subject"]
        corg= request.POST["organisation"]
        cdes= request.POST["designation"]
        cach= request.POST["achievments"]
        se=request.POST['section']
     
        imgup = request.POST["imgupdate"]
        
        hashpass = hashlib.md5(cpass.encode('utf8')).hexdigest()
        
        imgupDOC= request.POST["imgupdatedoc"]
        print(imgup, "***********")
        if imgup == "Yes":
            image1 = request.FILES['image']
            oldrec =teacher_tb.objects.all().filter(id=up)
            uprec = teacher_tb.objects.get(id=up)
            for x in oldrec:
                imgurl = x.photo.url
                pathtoimage = os.path.dirname(
                    os.path.dirname(os.path.abspath(__file__)))+imgurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print("successfully removed")
            uprec.photo = image1
            uprec.save()
       
        if imgupDOC == "Yes":
            imagedoc1 = request.FILES['doc']
            oldrecdoc =teacher_tb.objects.all().filter(id=up)
            uprecdoc = teacher_tb.objects.get(id=up)
            for x in oldrecdoc:
                imgurldoc = x.document.url
                pathtoimagedoc = os.path.dirname(
                    os.path.dirname(os.path.abspath(__file__)))+imgurldoc
                if os.path.exists(pathtoimagedoc):
                    os.remove(pathtoimagedoc)
                    print("successfully removed")
            uprecdoc.document = imagedoc1
            uprecdoc.save()
       
        teacher_tb.objects.filter(id=up).update(section=se,name=cname,hpassword=hashpass,email=cmail,password=cpass,dob=cdob,qualification=cqualification,experience=cexp,subject=csub,organisationaddress=corg,designation=cdes,achievments=cach, address=caddress,gender=cgen,fathername=cfname,mothername=cmname,phone=cphone)
        return render(request, "adminindex.html")
    else:
         return render(request, "adminindex.html")

def deleteteacher(request):
    ii = request.GET['id']
    query = teacher_tb.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/adminindex/')
def editteacher(request):
    ii = request.GET['id']
    query =  teacher_tb.objects.filter(id=ii)
    return render(request, "updateteach.html", {'usr': query})

def feedetail(request):
    
    if request.method == 'POST':

        ctype = request.POST["feetype"]
        cclass = request.POST["class"]
        camount = request.POST["amount"]

        add = fee_tb(feetype=ctype,clas=cclass,feeamount=camount,status='')
       


        check=fee_tb.objects.filter(feetype=ctype,clas=cclass,feeamount=camount,status='',period="quarter1")
        if check:
            
            add1 = fee_tb(feetype=ctype,clas=cclass,feeamount=camount,status='',period="quarter2")
            add1.save()
            return HttpResponseRedirect('/')
        else:
            add.save()
            return HttpResponseRedirect('/')
    else:

        return render(request, "feedetail.html")


def addcourse(request):
    if request.method=="POST":
        
      course=request.POST["course"]
      
      course_model=course_tb(coursename=course)
      course_model.save()
           
      return HttpResponseRedirect('/myadmin/')
    else:
      return render(request,'addcourse.html')
def editcourse(request):
    ii=request.GET['id']
    q=course_tb.objects.filter(id=ii)
    return render(request,'updatecourse.html',{'q':q})
def updatecourse(request):
      ii=request.GET['id']
      if request.method == 'POST':
       course=request.POST["course"]
      
       course_tb.objects.filter(id=ii).update(coursename=course)
   
           
       return HttpResponseRedirect('/myadmin/')
      else:
       return render(request,'updatecourse.html')



def managestudentleaveadmin(request):
  
    query1=leave_report_student.objects.all()
      
    


    return render(request,"managestudentleaveadmin.html",{"reg":query1})
    
def approveleave(request):
    ii=request.GET['id']
    query=leave_report_student.objects.filter(id=ii).update(status='approved')
    query1=leave_report_student.objects.filter(status='pending')
    return  render(request,'managestudentleaveadmin.html',{"reg":query1})
   
  
def rejectleave(request):
    ii=request.GET['id']
    query=leave_report_student.objects.filter(id=ii).update(status='rejected')
    query1=leave_report_student.objects.filter(status='pending')
   
    return  render(request,'managestudentleaveadmin.html',{"reg":query1})
def manageteacherleave(request):
  
    query1=leave_report_teacher.objects.all()
      
    


    return render(request,"manageteacherleave.html",{"reg":query1})
    
def approveleaveteacher(request):
    ii=request.GET['id']
    query=leave_report_teacher.objects.filter(id=ii).update(status='approved')
    query1=leave_report_teacher.objects.filter(status='pending')
    return  render(request,'manageteacherleave.html',{"reg":query1})
   
  
def rejectleaveteacher(request):
    ii=request.GET['id']
    query=leave_report_teacher.objects.filter(id=ii).update(status='rejected')
    query1=leave_report_teacher.objects.filter(status='pending')
   
    return  render(request,'manageteacherleave.html',{"reg":query1})
def manageattendance(request):
    s=student_tb.objects.filter(standard='11',feetype='A')
    s1=student_tb.objects.filter(standard='12',feetype='B')
    return render(request,'managestudentattendance.html',{'s':s,'s1':s1})

def attendancepage(request):
    ii=request.GET['id']
    q=student_tb.objects.filter(id=ii)
    return render(request,'attendance.html',{'q':q})
def studentattendance(request):
      ii=request.GET['id']

      s=student_tb.objects.filter(id=ii)
      student=student_tb.objects.get(id=ii)

      if request.method == 'POST':

        ctotal = request.POST["total"]
        cmon= request.POST["month"]
        status=request.POST['status']

        catt = request.POST["attended"]
        check=attendance_student_tb.objects.filter(studentid=student,month=cmon)
        if check:
               return render(request, "attendance.html", {'msg':"STUDENT ALREADY ADDED"})
        else:
       

       
   

              add = attendance_student_tb(status=status,studentid=student,month=cmon,total_lec=ctotal,lec_attended=catt)

              add.save()
              return HttpResponseRedirect('/myadmin/')
      else:
       


      
    

       return render(request,"attendance.html")
          

          


def addsubjectpage(request):
    courses=course_tb.objects.all()
    staffs=teacher_tb.objects.all()
    return render(request,"subjectadd.html",{"staffs":staffs,"courses":courses})

   
def subjectadd(request):
  

    
    if request.method == 'POST':

        csub = request.POST["subject_name"]
        cid=request.POST.get('course')
        course=course_tb.objects.get(id=cid)
        sid=request.POST.get('staff')
        staff=teacher_tb.objects.get(id=sid)
        


        
        add=subject_tb(subjectname=csub,teacherid=staff,courseid=course)
        add.save()
        return HttpResponseRedirect('/myadmin/')
    else:
        return render(request,'subjectadd.html')
def managesubject(request):
    q=subject_tb.objects.all()
    return render(request,'managesubject.html',{"reg":q})
def managecourse(request):
    q=course_tb.objects.all()
    return render(request,'managecourse.html',{"reg":q})

def editsubject(request):
    ii = request.GET['id']
    query =  subject_tb.objects.filter(id=ii)
    courses=course_tb.objects.all()
    staffs=teacher_tb.objects.all()
    return render(request, "subjectupdate.html", {'usr': query,"staffs":staffs,"courses":courses})

def updatesubject(request):
    
    ii=request.GET['id']
    if request.method == 'POST':

        csub = request.POST["subject_name"]
        cid=request.POST.get('course')
        course=course_tb.objects.get(id=cid)
        sid=request.POST.get('staff')
        staff=teacher_tb.objects.get(id=sid)

        subject_tb.objects.filter(id=ii).update(subjectname=csub,teacherid=staff,courseid=course)
        return HttpResponseRedirect('/myadmin/')
    else:
        return render(request,'subjectupdate.html')
def approvesubject(request):
    ii=request.GET['id']
    query=subject_tb.objects.filter(id=ii).update(status='approved')
    query1=subject_tb.objects.filter(status='pending')
    return  render(request,'adminindex.html',{"reg":query1})

def approvecourse(request):
    ii=request.GET['id']
    query=course_tb.objects.filter(id=ii).update(status='approved')
    query1=course_tb.objects.filter(status='pending')
    return  render(request,'adminindex.html',{"reg":query1})


def deletesubject(request):
    
    ii=request.GET['id']
    subject_tb.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/adminindex/')
def deletecourse(request):
    
    ii=request.GET['id']
    course_tb.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/adminindex/')
def addsessionpage(request):
    
    return render(request,"session.html")
def addsess(request):
    if request.method=="POST":
        
      ss=request.POST["start"]
      se=request.POST["end"]
      
      add=sessionyear_tb(session_start_year=ss,session_end_year=se)
      add.save()

           
      return HttpResponseRedirect('/myadmin/')
    else:
      return render(request,'session.html')
def managefee(request):
    q=fee_tb.objects.all()
    return render(request,'managefee.html',{"usr":q})

def timetablepage(request):
    q=subject_tb.objects.all()
    return render(request,'addtimetable.html',{"staffs":q})
def addtimetable(request):
    if request.method == 'POST':
        cc=request.POST["class"]
        div=request.POST["division"]
        p1=request.POST['p1']
        p2=request.POST['p2']
        p3=request.POST['p3']
        p4=request.POST['p4']
        p5=request.POST['p5']
        day=request.POST['day']
        

        
        add=timetable(day=day,clas=cc,div=div,period1=p1,period2=p2,period3=p3,period4=p4,period5=p5)
        add.save()
        return HttpResponseRedirect('/myadmin/')
    else:
        return render(request,'addtimetable.html')
def managetimetable(request):
    q=timetable.objects.all()
    return render(request,"managetimetable.html",{'usr':q})

def deletetimetable(request):
    ii=request.GET['id']
    timetable.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/myadmin/')


def editpagett(request):
    q=subject_tb.objects.all()
    ii=request.GET['id']
    q1=timetable.objects.filter(id=ii).all()
    return render(request,"ttupdate.html",{'usr':q1,'staffs':q})


def edittimetable(request):
    ii=request.GET['id']
    if request.method == 'POST':
        cc=request.POST["class"]
        div=request.POST["division"]
        p1=request.POST['p1']
        p2=request.POST['p2']
        p3=request.POST['p3']
        p4=request.POST['p4']
        p5=request.POST['p5']
        day=request.POST['day']
      

        timetable.objects.filter(id=ii).update(day=day,clas=cc,div=div,period1=p1,period2=p2,period3=p3,period4=p4,period5=p5)
        return HttpResponseRedirect('/myadmin/')
    else:
           return render(request,'ttupdate.html')



def salarydetail(request):
    
    if request.method == 'POST':

        ctype = request.POST["type"]
    
        camount = request.POST["amount"]

        add = salary(salarytype=ctype,allowance=camount,status='')
        add.save()
        return HttpResponseRedirect('/myadmin/')
        
    else:

        return render(request, "salarydetail.html")
def managesalary(request):
    t=teacher_tb.objects.all()
    return render(request,"managesalary.html",{"t":t})

def paysalary(request):
        ii=request.GET['id']
        
        t=teacher_tb.objects.filter(id=ii)
        q=teacher_tb.objects.get(id=ii)
        for i in t:
            s=i.section
        
        sal=salary.objects.filter(salarytype=s)
        for x in sal:
            amount=x.allowance
        if sal:
            if request.method=="POST":
         
             amount=request.POST['amount']
             x=datetime.datetime.now()
             mon=request.POST['month']
             check=salary.objects.filter(teacherid=q,allowance=amount,status="paid",month=mon)
             if check:
               return render(request, "paysalary.html", {'msg':"paid "})
             else:
              add=salary(teacherid=q,allowance=amount,date=x,status="paid",month=mon,salarytype=s)
              add.save()
       

              return HttpResponseRedirect('/myadmin/')
            else:
             return render(request, "paysalary.html",{'t':t,'amount':amount})



def manageresult(request):
    s=student_tb.objects.filter(standard='11',feetype='A')
    s1=student_tb.objects.filter(standard='12',feetype='B')
    return render(request,'addresult.html',{'s':s,'s1':s1})
      
def addresult(request):
    ii=request.GET['id'] 
    q=student_tb.objects.filter(id=ii)
    student=student_tb.objects.get(id=ii)
    subject=subject_tb.objects.all()
    if request.method=="POST":
        sem=request.POST['sem']
        type=request.POST['type']
        total=request.POST['ts']
        ss=request.POST['ss']
        s1=request.POST['subject1']
        s2=request.POST['subject2']
        s3=request.POST['subject3']
        s4=request.POST['subject4']
        s5=request.POST['subject5']
        ag=request.POST['g']
        grade=request.POST['grade']
        status=request.POST['status']
        add=StudentResult(status=status,studentid=student,subject1=s1,subject2=s2,subject3=s3,subject4=s4,subject5=s5,subject_assignment_marks=ag,grade=grade,examtype=type,totalmark=total,studentmark=ss,sem=sem)
        c=StudentResult.objects.filter(studentid=student,examtype=type,sem=sem)
      
        if c:
         
            return render(request, "addresult.html",{'msg':'result added already'})
        else:
            add.save()
            
            return HttpResponseRedirect('/myadmin/')
       
    else:
             return render(request, "examresult.html",{'subject':subject,'s':q})
    

def resultrec(request):
    q=StudentResult.objects.all()
    return render(request,'resultrecord.html',{'q':q})


def editresult(request):
    ii=request.GET['id']
    q=StudentResult.objects.filter(id=ii)
    return render(request,'updateresult.html',{'q':q})
def deleteresult(request):
    ii=request.GET['id']
    q=StudentResult.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/myadmin/')
def updateresult(request):
    ii=request.GET['id']

  
   
  
    if request.method=="POST":
        sem=request.POST['sem']
        type=request.POST['type']
        total=request.POST['ts']
        ss=request.POST['ss']
        s1=request.POST['subject1']
        s2=request.POST['subject2']
        s3=request.POST['subject3']
        s4=request.POST['subject4']
        s5=request.POST['subject5']
        ag=request.POST['g']
        grade=request.POST['grade']
        status=request.POST['status']
        StudentResult.objects.filter(id=ii).update(status=status,subject1=s1,subject2=s2,subject3=s3,subject4=s4,subject5=s5,subject_assignment_marks=ag,grade=grade,examtype=type,totalmark=total,studentmark=ss,sem=sem)
        
          
            
        return HttpResponseRedirect('/myadmin/')
       
    else:
             return render(request, "updatesult.html")
def attendancerecord(request):
    q=attendance_student_tb.objects.all()
    return render(request,'attendancerecordstudent.html',{'reg':q})
def editattendancestudent(request):
    ii=request.GET['id']
    q=attendance_student_tb.objects.filter(id=ii)
    return render(request,'updateattendancestud.html',{'q':q})

def updatestudentattendance(request):
     ii=request.GET['id']

  
   
  
     if request.method=="POST":
        ctotal = request.POST["total"]
        cmon= request.POST["month"]
        status=request.POST['status']

        catt = request.POST["attended"]
        attendance_student_tb.objects.filter(id=ii).update(status=status,month=cmon,total_lec=ctotal,lec_attended=catt)
          
            
        return HttpResponseRedirect('/myadmin/')
       
     else:
             return render(request, "updateattendancestud.html")
def delattendancerecord(request):
       ii=request.GET['id']
       attendance_student_tb.objects.filter(id=ii).delete()
       
       return HttpResponseRedirect('/myadmin/')


def staffregistration(request):


    if request.method == 'POST':

        cname = request.POST["name"]

        
        
        cimg = request.FILES["image"]
        cdob = request.POST["dob"]
       
        caddress = request.POST["address"]
        cgen= request.POST["gender"]
        cfname = request.POST["fname"]
        cmname = request.POST["mname"]
        cphone = request.POST["phone"]
       
        se=request.POST['section']
     
        
        
      
       
        add = staff(section=se,name=cname,photo=cimg,dob=cdob, address=caddress,gender=cgen,fathername=cfname,mothername=cmname,phone=cphone)
        add.save()
        return render(request, "adminindex.html")
    else:

        return render(request, "staff.html")
    

def managestaff(request):
  
    query1=staff.objects.all()
      
    


    return render(request,"managestaff.html",{"reg":query1,})


def statusstaff(request):
    ii=request.GET['id']
    query=staff.objects.filter(id=ii).update(status='approved')
    query1=staff.objects.filter(status='pending')
    return  render(request,'managestaff.html',{"reg":query1})
def updatestaff(request):
    up = request.GET['id']



    if request.method == 'POST':

        cname = request.POST["name"]

       
    
        caddress = request.POST["address"]
     
        cdob = request.POST["dob"]
        
        cgen= request.POST["gender"]
        cfname = request.POST["fname"]
        cmname = request.POST["mname"]
        cphone = request.POST["phone"]
       
        se=request.POST['section']
     
        imgup = request.POST["imgupdate"]
        
        
        
 
        print(imgup, "***********")
        if imgup == "Yes":
            image1 = request.FILES['image']
            oldrec =staff.objects.all().filter(id=up)
            uprec = staff.objects.get(id=up)
            for x in oldrec:
                imgurl = x.photo.url
                pathtoimage = os.path.dirname(
                    os.path.dirname(os.path.abspath(__file__)))+imgurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print("successfully removed")
            uprec.photo = image1
            uprec.save()
       
       
        staff.objects.filter(id=up).update(section=se,name=cname,dob=cdob, address=caddress,gender=cgen,fathername=cfname,mothername=cmname,phone=cphone)
        return render(request, "adminindex.html")
    else:
         return render(request, "updatestaff.html")

def deletestaff(request):
    ii = request.GET['id']
    query = staff.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/adminindex/')
def editstaff(request):
    ii = request.GET['id']
    query =  staff.objects.filter(id=ii)
    return render(request, "updatestaff.html", {'usr': query})




def examdetail(request):
    if request.method == 'POST':
        cc=request.POST["clas"]
        e=request.POST["exam"]
        d=request.POST['date']
        t=request.POST['time']
       

        
        add=notice(standard=cc,exam=e,time=t,date=d)
        # print(cc,"%%")
        add.save()
        return HttpResponseRedirect('/myadmin/')
    else:
        return render(request,'examdetail.html')

    
          
def  updateexamdetail(request):
    up = request.GET['id']
    if request.method == 'POST':
        cc=request.POST["clas"]
        e=request.POST["exam"]
        d=request.POST['date']
        t=request.POST['time']
       

        
        notice.object.filter(id=up).update(standard=cc,date=d,exam=e,time=t)
       
        return HttpResponseRedirect('/myadmin/')
    else:
        return render(request,'addtimetable.html')



          
        
    
def deleteexam(request):
    ii = request.GET['id']
    query = notice.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/adminindex/')
def editexam(request):
    ii = request.GET['id']
    query = notice .objects.filter(id=ii)
    return render(request, "updateexamdetails.html", {'reg': query}) 
        
     
      
def statusexam(request):
    ii=request.GET['id']
    query=notice.objects.filter(id=ii).update(status='approved')
    query1=notice.objects.filter(status='pending')
    return  render(request,'manageexam.html',{"reg":query1})

def manageexam(request):
  
    query1=notice.objects.all()
      
    


    return render(request,"manageexam.html",{"reg":query1})








    