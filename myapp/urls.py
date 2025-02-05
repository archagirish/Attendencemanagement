
from django.urls import path
from .views import *
from myapp import views


urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', dashboard.as_view(), name='dashboard'),
    path('changepass/',Pass.as_view(), name='changepass'),
    path('notification/',Notification.as_view(),name='notification'),
    # path('notification/',Notifi.as_view(),name='notification'),
    # ////////////////////////////////////// ADMIN //////////////////////////////////////

    path('add_course/', Course.as_view(), name='add_course'),
    path('adddept/', Dept.as_view(),name='adddept'),
    path('complaint/', Complaint.as_view(),name='complaint'),
    path('edit_complaint/', Editcomp.as_view(),name='edit_complaint'),
    path('edit_notification/', Editnotification.as_view(),name='edit_notification'),
    path('manage_complaint/', Managecomp.as_view(),name='manage_complaint'),
    path('manage_couse/', Managecourse.as_view(),name='manage_couse'),
    path('delete_course/<int:pk>',Deletecourse.as_view(),name='delete_course'),
    path('edit_course/<int:pk>',Editcourse.as_view(),name='edit_course'),
    path('manage_dept/', Managedept.as_view(),name='manage_dept'),
    path('delete_department/<int:pk>',Deletedept.as_view(),name='delete_department'),
    path('edit_department/<int:pk>',Editdept.as_view(),name='edit_department'),
    path('managenotification/', Managenotification.as_view(),name='managenotification'),
    path('delete/<int:pk>', Deletenotification.as_view(),name="delete"),
    path('edit/<int:pk>',Editnotification.as_view(),name="edit"),
    path('manage_student/', Managestudent.as_view(),name='manage_student'),
    path('editstudent/<int:pk>',Editstudent.as_view(),name="editstudent"),
    path('deletestudent/<int:pk>',Deletestudent.as_view(),name='deletestudent'),
    path('manage_teacher/', Manageteacher.as_view(),name='manage_teacher'),
    path('editteacher/<int:pk>',Editteacher.as_view(),name="editteacher"),
    path('deleteteacher/<int:pk>',Deleteteacher.as_view(),name="deleteteacher"),
    path('student/', Student.as_view(),name='student'),
    path('teacher/', Teacher.as_view(),name='teacher'),
    path('subject/', Subject.as_view(),name='subject'),
    path('managesubject/',Managesubject.as_view(),name='managesubject'),
    path('search_subject/',search_subject.as_view(),name='search_subject'),
    path('delete_subject/<int:pk>', Deletesubject.as_view(),name='deletesubject'),
    path('reply/<int:pk>',reply.as_view(),name="reply"),
    path('deptsem', Dept_sem.as_view(),name='deptsem'),
    path('manage_class',Class.as_view(),name='manage_class'),
    path('addclass',Addclass.as_view(),name='addclass'),
    path('delete_class/<int:pk>',delete_class.as_view(),name="delete_class"),
    
    
    # //////////////////////////////////////// TEACHER ///////////////////////////////////


path('teacher_dashboard/', Teacher_dashboard.as_view(),name='teacher_dashboard'),
path('add_report/', Add_report.as_view(),name='add_report'),
path('edit_profile/', Edit_profile.as_view(),name='edit_profile'),
path('edit_report/', Edit_report.as_view(),name='edit_report'),
path('manage_attendance/', Manage_attendence.as_view(),name='manage_attendence'),
path('manage_report/', Manage_report.as_view(),name='manage_report'),
path('manage_subjectallocated/', Manage_subjectallocated.as_view(),name='manage_subjectallocated'),
path('manage_timtable/', Manage_timtable.as_view(),name='manage_timtable'),
path('mangeprofile/', Manageprofile.as_view(),name='mangeprofile'),
path('profile/', Profile.as_view(),name='profile'),
path('view_staff/', View_staff.as_view(),name='view_staff'),
path('view_student/', View_student.as_view(),name='view_student'),
path('viewnotification/', Viewnotification.as_view(),name='viewnotification'),
path('select_class_staff/', select_class_staff.as_view(),name='select_class_staff'),
path('manage_timetable', manage_timetable.as_view(),name='manage_timetable'),
path('add_timetable_action', add_timetable_action.as_view(),name='add_timetable_action'),
path('select_class_staff1', select_class_staff1.as_view(),name='select_class_staff1'),
path('view_timetable', view_timetable.as_view(),name='view_timetable'),
path('view_attendace_staff', view_attendace_staff.as_view(),name='view_attendace_staff'),
path('select_slot', select_slot.as_view(),name='select_slot'),
path('take_attendance', take_attendance.as_view(),name='take_attendance'),
path('leave/',Leave.as_view(),name='leave'),
path('accept_leave/<int:r_id>',accept_leave.as_view(),name='accept_leave'),
path('reject_leave/<int:r_id>',reject_leave.as_view(),name='reject_leave'),
# //////////////////////////// API /////////////////////////////////////////

    path('StudentReg', views.StudentReg.as_view(), name="StudentReg"),
    path('login_code', views.LoginPageApi.as_view(), name="login_code"),
    path('ViewTimeTable/<int:lid>', views.ViewTimeTable.as_view(), name="ViewTimeTable"),
    path('ViewAttendanceApi/<int:lid>', views.ViewAttendanceApi.as_view(), name="ViewAttendanceApi"),
    path('ViewProfileApi/<int:lid>', views.ViewProfileApi.as_view(), name="ViewProfileApi"),
    path('NotificationApi', views.NotificationApi.as_view(), name="NotificationApi"),
    path('SendComplaintApi/<int:lid>', views.SendComplaintApi.as_view(), name="SendComplaintApi"),
]