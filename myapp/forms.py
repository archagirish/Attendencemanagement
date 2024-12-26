
from django.forms import ModelForm

from .models import *


class Notification_form(ModelForm):
    class Meta:
        model= Notification_model
        fields=['Notification']

class Department_form(ModelForm):
    class Meta:
        model= DepartmentTable
        fields=['Dept_Name']     

class Course_form(ModelForm):
    class Meta:
        model=CourseTable
        fields=['CourseName'] 

class Adduser_form(ModelForm):
    class Meta:
        model=StudentTable
        fields=['name','email','phonenumber','DEPARTMENT']  

class Teacher_form(ModelForm):
    class Meta:
        model= TeacherTable
        fields=['name','email','phonenumber','DEPARTMENT'] 

class Subject_form(ModelForm):
    class Meta:
        model= SubjectTable
        fields=['subject']

class Addreport(ModelForm):
    model= ReportTable
    fields=['date','report','reply']

class Complaint_form(ModelForm):
    model= ComplaintTable
    fields=['date','complaint','reply','report']

    # ///////////////////////////////////////////// TEACHER ///////////////////////////////////////////
    
class Attendance_form(ModelForm):
    model = AttendanceTable
    fields =['day','hour'] 



