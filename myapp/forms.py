
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
        fields=['name','email','phonenumber','department']     



