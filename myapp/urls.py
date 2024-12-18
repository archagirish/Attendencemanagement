
from django.urls import path
from .views import *


urlpatterns = [
    path('', Login.as_view(), name='login'),
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
    path('student/', Student.as_view(),name='student'),
    path('teacher/', Teacher.as_view(),name='teacher'),
    
    
    # //////////////////////////////////////// TEACHER ///////////////////////////////////


path('add_report/', Add_report.as_view(),name='report'),
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



]