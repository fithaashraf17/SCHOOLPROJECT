from atexit import register
from cgitb import html
import email
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




def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")
def gallery(request):
    return render(request,"gallery.html")
def services(request):
    return render(request,"services.html")
def typography(request):
    return render(request,"typography.html")
def loginstudent(request):
    if request.method=="POST":
        
      
       cname=request.POST["name"]   
       cpass=request.POST["password"]
       print(cpass,"))))))")
       hashpass=hashlib.md5(cpass.encode('utf8')).hexdigest()
       print(hashpass,"*****************")


       log=student_tb.objects.filter(name=cname,hpassword=hashpass)
       if log:
           for x in log:
               request.session["myid"]=x.id
               request.session["myname"]=x.name
               ii=request.session["myid"]
            #    request.session["img"]=x.image.url
               uid = student_tb.objects.filter(id=ii)
               if uid:
                   return render(request,"index.html")
               else:
                    

   
                 return render(request,'login.html')
       else:
          return render(request,'login.html',{"msg":"invalid credentials"})

    else:
        return render(request,'login.html')
def loginteach(request):
    if request.method=="POST":
        
      
       cname=request.POST["name"]   
       cpass=request.POST["password"]
       print(cpass,"))))))")
       hashpass=hashlib.md5(cpass.encode('utf8')).hexdigest()
       print(hashpass,"*****************")


       log=teacher_tb.objects.filter(name=cname,hpassword=hashpass)
       if log:
           for x in log:
               request.session["teachid"]=x.id
               request.session["teachname"]=x.name
               ii=request.session["teachid"]
            #    request.session["img"]=x.image.url
            #    uid = teacher_tb.objects.filter(id=ii)
            #    if uid:
               return render(request,"index.html")
            #    else:
                    

   
            #       return render(request,'loginteach.html')
       else:
           return render(request,"loginteach.html",{"msg":"invalid credentials"})
    else:
        return render(request,"loginteach.html")
def logout(request):
    if request.session.has_key('myid'):
        del request.session["myid"]
        del request.session["myname"]
        logout(request)
        return HttpResponseRedirect('/')
    elif request.session.has_key('teachid'):
        del request.session["teachid"]
        del request.session["teachname"]
        logout(request)
        return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')
def myaccount(request):
     if request.session.has_key('myid'):
         ii=request.session['myid']
         q=student_tb.objects.filter(id=ii)
      
         
         return render(request,"myaccount.html",{"reg":q})
     else:
         return HttpResponseRedirect('/')
def myaccountteach(request):
     if request.session.has_key('teachid'):
         ii=request.session['teachid']
         q=teacher_tb.objects.filter(id=ii)
      
         
         return render(request,"myaccountteach.html",{"reg":q})
     else:
         return HttpResponseRedirect('/')




def changepass(request):
        ii=request.session['myid']
        q=student_tb.objects.filter(id=ii)
        if request.method=="POST":
         oldpass=request.POST['password']
         newpass=request.POST['newpassword']
         check=student_tb.objects.filter(id=ii)
         for x in check:
            password=x.password
         if password==oldpass:
            hashpass=hashlib.md5(newpass.encode('utf8')).hexdigest()
            student_tb.objects.filter(id=ii).update(password=newpass,hpassword=hashpass)
            return HttpResponseRedirect('/logout/')
         else:
            return render(request,"changepassword.html",{'usr':q,"msg":"invalid"})
        else:
              return render(request,"changepassword.html",{'usr':q})
def changepassteach(request):
        ii=request.session['teachid']
        q=teacher_tb.objects.filter(id=ii)
        if request.method=="POST":
         oldpass=request.POST['password']
         newpass=request.POST['newpassword']
         check=teacher_tb.objects.filter(id=ii)
         for x in check:
            password=x.password
         if password==oldpass:
            hashpass=hashlib.md5(newpass.encode('utf8')).hexdigest()
            teacher_tb.objects.filter(id=ii).update(password=newpass,hpassword=hashpass)
            return HttpResponseRedirect('/logout/')
         else:
            return render(request,"changepasswordteach.html",{'usr':q,"msg":"invalid"})
        else:
              return render(request,"changepasswordteach.html",{'usr':q})


def payfee(request):
    ii=request.session['myid']
    

    q =student_tb.objects.get(id=ii)
    stud =student_tb.objects.filter(id=ii)

   
    for x in stud:
        c=x.standard
    fees=fee_tb.objects.filter(clas=c,feetype='ACADEMIC FEE')
    for x in fees:
        feeinfo=x.feeamount
    
    if feeinfo:
     if request.method=="POST":
         
         amount=request.POST['amount']
         x=datetime.datetime.now()
        #  add=fee_tb(studentid=q,feeamount=amount,date=x,status="paid")
        #  add.save()
       
         check=fee_tb.objects.filter(studentid=q,feeamount=amount,status="paid",period="quarter1",feetype='ACADEMIC FEE')
         check1=fee_tb.objects.filter(studentid=q,feeamount=amount,status="paid",period="quarter2",feetype='ACADEMIC FEE')
         if check and check1:
              return render(request, "feepay.html", {'msg':"paid "})
         else:

          if check:
            
            add1=fee_tb(studentid=q,feeamount=amount,date=x,status="paid",period="quarter2",feetype='ACADEMIC FEE')
            add1.save()
            return HttpResponseRedirect('/')
          else:
            add=fee_tb(studentid=q,feeamount=amount,date=x,status="paid",feetype='ACADEMIC FEE')
            add.save()
       

            return HttpResponseRedirect('/')

        

            

         
     else:
        return render(request, "feepay.html", {'usr':stud,"fee":feeinfo})
        
def examfee(request):
    ii=request.session['myid']
    

    q =student_tb.objects.get(id=ii)
    stud =student_tb.objects.filter(id=ii)

   
    for x in stud:
        c=x.standard
    fees=fee_tb.objects.filter(clas=c,feetype='EXAM FEE')
    for x in fees:
        feeinfo=x.feeamount
        fe=x.feetype
    if feeinfo:
     if request.method=="POST":
         
         amount=request.POST['amount']
         x=datetime.datetime.now()
        #  add=fee_tb(studentid=q,feeamount=amount,date=x,status="paid")
        #  add.save()
       
         check=fee_tb.objects.filter(studentid=q,feeamount=amount,status="paid",period="quarter1",feetype='EXAM FEE')
         
         check1=fee_tb.objects.filter(studentid=q,feeamount=amount,status="paid",period="quarter2",feetype='EXAM FEE')
       
         if check and check1:
              return render(request, "feepay.html", {'msg':"paid "})
         else:

          if check:
            
            add1=fee_tb(studentid=q,feeamount=amount,date=x,status="paid",period="quarter2",feetype='EXAM FEE')
            add1.save()
            return HttpResponseRedirect('/')
          else:
            add=fee_tb(studentid=q,feeamount=amount,date=x,status="paid",feetype='EXAM FEE')
            add.save()
       

            return HttpResponseRedirect('/')

        

            

         
     else:
        return render(request, "examfee.html", {'usr':stud,"fee":feeinfo})
        

def leavestudent(request):
     if request.session.has_key('myid'):
         ii=request.session['myid']
         stud =student_tb.objects.filter(id=ii)
       
         q =student_tb.objects.get(id=ii)
         
         if request.method=="POST":
          creason=request.POST['reason']
          x=datetime.datetime.now()
          add=leave_report_student(studentid=q,leavedate=x,leave_message=creason)
          add.save()
           
          return HttpResponseRedirect('/')
         else:
             return render(request,"leavestudent.html",{"usr":stud})
        
          

          


      
         
         
     else:
         return render(request,"login.html")
def leaveteacher(request):
     if request.session.has_key('teachid'):
         ii=request.session['teachid']
         stud =teacher_tb.objects.filter(id=ii)
       
         q =teacher_tb.objects.get(id=ii)
         
         if request.method=="POST":
          creason=request.POST['reason']
          x=datetime.datetime.now()
          add=leave_report_teacher(teacherid=q,leavedate=x,leave_message=creason)
          add.save()
           
          return HttpResponseRedirect('/')
         else:
          return render(request,"leaveteacher.html",{"usr":stud})
        
          

          


      
         
         
     else:
         return render(request,"loginteach.html")
         
def managestudentleave(request):
 if request.session.has_key('teachid'):


  
    query1=leave_report_student.objects.all()
      
    


    return render(request,"managestudentleave.html",{"reg":query1})
 else:
     return render(request,"loginteach.html",{"msg":"Invalid credentials"})

    
def approveleave(request):
    ii=request.GET['id']
    query=leave_report_student.objects.filter(id=ii).update(status='approved')
    query1=leave_report_student.objects.filter(status='pending')
    return  render(request,'managestudentleave.html',{"reg":query1})
   
  
def rejectleave(request):
    ii=request.GET['id']
    query=leave_report_student.objects.filter(id=ii).update(status='rejected')
    query1=leave_report_student.objects.filter(status='pending')
  

   
    return  render(request,'adminindex.html',{"reg":query1})
def timetablepage(request):
    q=timetable.objects.filter(clas='11',div='A')
    q1=timetable.objects.filter(clas='12',div='A')

    return  render(request,'timetable.html',{"reg":q,"reg1":q1})

        
def attendancepagetea(request):
  if request.session.has_key('teachid'):
         ii=request.GET['id']
         q=student_tb.objects.filter(id=ii)

         return render(request,'attendancetea.html',{'q':q})
  else:
         return render(request,"loginteach.html")
 
def studentattendancetea(request):
     

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
               return render(request, "attendancetea.html", {'msg':"STUDENT ALREADY ADDED"})
        else:
       

       
   

              add = attendance_student_tb(status=status,studentid=student,month=cmon,total_lec=ctotal,lec_attended=catt)

              add.save()
              return HttpResponseRedirect('/')

      else:
       


      
    

       return render(request,"attendance.html")
    


          

def manageattendancetea(request):
    if request.session.has_key('teachid'):

     s=student_tb.objects.filter(standard='11',feetype='A')
     s1=student_tb.objects.filter(standard='12',feetype='B')
     return render(request,'managestudentattendancetea.html',{'s':s,'s1':s1})
    else:
     return render(request,"loginteach.html")

def studentleavestatus(request):
    if request.session.has_key('myid'):
         ii=request.session['myid']
         stud =leave_report_student.objects.filter(studentid=ii)
         return render(request,'statusofleavestudent.html',{'reg':stud})
    else:
         return render(request,'statusofleavestudent.html')



def teachleavestatus(request):
    if request.session.has_key('teachid'):
         ii=request.session['teachid']
         t =leave_report_teacher.objects.filter(teacherid=ii)
         
         return render(request,'leavestatusteach.html',{'reg':t})
    else:
         return render(request,"loginteach.html")


def resultrec(request):
    if request.session.has_key('teachid'):
  

     q=StudentResult.objects.all()
     return render(request,'resultrec.html',{'q':q})
    else:
     return render(request,'loginteach.html')

def result(request):
    if request.session.has_key('myid'):
         ii=request.session['myid']
         s=StudentResult.objects.filter(studentid=ii)
         if request.method=='POST':

          register=request.POST['reg']
          c=student_tb.objects.filter(id=ii,regno=register)
          if c:
              return render(request,'result.html',{'s':s})
          else:
              return render(request,'index.html',{'msg':"Invalid details"})
         else:
          return render(request,'resultpage.html')
    else:
         return render(request,'login.html')
def appointment(request):
    if request.method=="POST":
         fname=request.POST['First Name']
         lname=request.POST['Last Name']
         email=request.POST['Email']
         p=request.POST['Phone']
         d=request.POST['date']
         add=contact(fname=fname,lname=lname,email=email,phone=p,date=d)
         add.save()
         return HttpResponseRedirect('/')
    else:
         return request("index.html")

        
def noticeforexam(request):
    s=notice.objects.all()
    return render(request,'examdetails.html',{"s":s})

        
