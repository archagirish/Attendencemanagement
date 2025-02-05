
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
        fields=['name','email','phonenumber', 'image']  

class Teacher_form(ModelForm):
    class Meta:
        model= TeacherTable
        fields=['name','email','phonenumber','DEPARTMENT'] 

class Subject_form(ModelForm):
    class Meta:
        model= SubjectTable
        fields=['subject']

class Addreport(ModelForm):
    class Meta:
        model= ReportTable
        fields=['date','report','reply']

class Complaint_form(ModelForm):
    class Meta:
        model= ComplaintTable
        fields=['date','complaint','reply']

    # ///////////////////////////////////////////// TEACHER ///////////////////////////////////////////
    
class TimeTable_form(ModelForm):
    class Meta:
        model = TimetableTable
        fields = ['Day', 'CLASS','hour','subject','sem', 'TEACHERID']

class Report_form(ModelForm):
    class Meta:
        model = ReportTable
        fields = ['date','report','reply']


