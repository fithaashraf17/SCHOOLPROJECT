from django.urls import path,include
from django import urls
from myapp import views

urlpatterns = [
  
    path("",views.index),

  
    
    path("changepass/",views.changepass),
    path("changepassteach/",views.changepassteach),

    path("about/",views.about),
    path("gallery/",views.gallery),
    path("services/",views.services),
    path("typography/",views.typography),
    path("loginstudent/",views.loginstudent),
    path("loginteach/",views.loginteach ),
    path("logout/",views.logout),
    path("myaccount/",views.myaccount),
    path("myaccountteach/",views.myaccountteach),
    path("payfee/",views.payfee),
    path("examfee/",views.examfee),
    path("leaveteacher/",views.leaveteacher),

    path("leavestudent/",views.leavestudent),
    path("managestudentleave/",views.managestudentleave),
    path("approveleave/",views.approveleave),
    path("rejectleave/",views.rejectleave),

    path("timetablepage/",views.timetablepage),
    path("studentattendancetea/",views.studentattendancetea),
    path("attendancepagetea/",views.attendancepagetea),
    path("studentleavestatus/",views.studentleavestatus),
    path("manageattendancetea/",views.manageattendancetea),
    path("teachleavestatus/",views.teachleavestatus),
    path("resultrec/",views.resultrec),
    path("appointment/",views.appointment),
    path("result/",views.result),
    path("noticeforexam/",views.noticeforexam),




    
 

    




   


]