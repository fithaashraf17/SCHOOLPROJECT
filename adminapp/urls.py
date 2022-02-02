from django.urls import path,include
from django import urls
from adminapp import views

urlpatterns = [
  
    path("",views.adminindex),
    path("inputs/",views.inputs),
 
    path("student_admission/",views.student_admission,name="student_admission"),
    path("managestudent/",views.managestudent,name="managestudent"),
    path("status/",views.status,name="status"),
    path("statustea/",views.statustea,name="statustea"),
    path("updatestudent/",views.updatestudent,name="updatestudent"),
    path("deletestudent/",views.deletestudent,name="deletestudent"),
    path("editstudent/",views.editstudent,name="editstudent"),
    path("teacherregistration/",views.teacherregistration,name="teacherregistration"),
    path("manageteacher/",views.manageteacher,name="manageteacher"),
    path("updateteacher/",views.updateteacher,name="updateteacher"),
    path("editteacher/",views.editteacher,name="editteacher"),
    path("deleteteacher/",views.deleteteacher,name="deleteteacher"),
    path("addcourse/",views.addcourse,name="addcourse"),
    path("manageattendance/",views.manageattendance,name="manageattendance"),
    path("attendancepage/",views.attendancepage,name="attendancepage"),

    path("feedetail/",views.feedetail,name="feedetail"),
    path("manageteacherleave/",views.manageteacherleave,name="manageteacherleave"),
    path("managestudentleaveadmin/",views.managestudentleaveadmin,name="managestudentleaveadmin"),
    path("approveleave/",views.approveleave,name="approveleave"),
    path("rejectleave/",views.rejectleave,name="rejectleave"),
    path("approveleaveteacher/",views.approveleaveteacher,name="approveleaveteacher"),
    path("rejectleaveteacher/",views.rejectleaveteacher,name="rejectleaveteacher"),
    
    
    path("addsubjectpage/",views.addsubjectpage,name="addsubjectpage"),
    path("subjectadd/",views.subjectadd,name="subjectadd"),
    path("managesubject/",views.managesubject,name="managesubject"),

    
    path("addsessionpage/",views.addsessionpage,name="addsessionpage"),
    
    path("addsess/",views.addsess,name="addsess"),

    path("updatesubject/",views.updatesubject,name="updatesubject"),
    path("studentattendance/",views.studentattendance,name="studentattendance"),
    path("deletesubject/",views.deletesubject,name="deletesubject"),
    path("editsubject/",views.editsubject,name="editsubject"),
    path("managefee/",views.managefee,name="managefee"),
    path("edittimetable/",views.edittimetable,name="edittimetable"),
    path("editpagett/",views.editpagett,name="editpagett"),
    path("deletetimetable/",views.deletetimetable,name="deletetimetable"),
    path("managetimetable/",views.managetimetable,name="managetimetable"),
    path("deletestudentfee/",views.deletestudentfee,name="deletestudentfee"),
    path("salarydetail/",views.salarydetail,name="salarydetail"),
    path("paysalary/",views.paysalary,name="paysalary"),
    path("addresult/",views.addresult,name="addresult"),
    path("manageresult/",views.manageresult,name="manageresult"),
    path("addtimetable/",views.addtimetable,name="addtimetable"),
    path("managesalary/",views.managesalary,name="managesalary"),
    path("timetablepage/",views.timetablepage,name="timetablepage"),
    path("editresult/",views.editresult,name="editresult"),
    path("deleteresult/",views.deleteresult,name="deleteresult"),
    path("updateresult/",views.updateresult,name="updateresult"),
    path("resultrec/",views.resultrec,name="resultrec"),
    path("editcourse/",views.editcourse,name="editcourse"),
     path("updatecourse/",views.updatecourse,name="updatecourse"),
    
    path("managecourse/",views.managecourse,name="managecourse"),

    path("deletecourse/",views.deletecourse,name="deletecourse"),
    path("approvecourse/",views.approvecourse,name="approvecourse"),
    path("attendancerecord/",views.attendancerecord,name="attendancerecord"),
    path("approvesubject/",views.approvesubject,name="approvesubject"),
    path("editattendancestudent/",views.editattendancestudent,name="editattendancestudent"),
    path("staffregistration/",views.staffregistration,name="staffregistration"),
    path("managestaff/",views.managestaff,name="managestaff"),
    path("updatestaff/",views.updatestaff,name="updatestaff"),
    path("editstaff/",views.editstaff,name="editstaff"),
    path("deletestaff/",views.deletestaff,name="deletestaff"),
    path("statusstaff/",views.statusstaff,name="statusstaff"),
    path("updatestudentattendance/",views.updatestudentattendance,name="updatestudentattendance"),
    path("delattendancerecord/",views.delattendancerecord,name="delattendancerecord"),

    path("deleteexam/",views.deleteexam,name="deleteexam"),
    path("examdetail/",views.examdetail,name="examdetail"),
    path("manageexam/",views.manageexam,name="manageexam"),
    path("updateexamdetail/",views.updateexamdetail,name="updateexamdetail"),
    path("editexam/",views.editexam,name="editexam"),
    path("deletestaff/",views.deletestaff,name="deletestaff"),
    path("statusexam/",views.statusexam,name="statusexam"),


    


 ]