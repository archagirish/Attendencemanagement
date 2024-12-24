from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    type= models.CharField(max_length=100,null=True,blank=True)

    
class DepartmentTable(models.Model):
    Dept_Name = models.CharField(max_length=100, null=True, blank=True)

class CourseTable(models.Model):
    department_id=models.ForeignKey(DepartmentTable,on_delete=models.CASCADE,null=True,blank=True)
    CourseName = models.CharField(max_length=100,null=True,blank=True)

class SubjectTable(models.Model):
    DEPARTMENT=models.ForeignKey(DepartmentTable,on_delete=models.CASCADE,null=True,blank=True)
    subject = models.CharField(max_length=250,null=True,blank=True)



class TeacherTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    DEPARTMENT = models.ForeignKey(DepartmentTable,on_delete=models.CASCADE,null=True,blank=True)
    SUBJECT=models.ForeignKey(SubjectTable,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    phonenumber = models.BigIntegerField(max_length=100,null=True,blank=True)



class  AttendanceTable(models.Model):
    StudentID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    day = models.CharField(max_length=100,null=True,blank=True)  
    hour = models.CharField(max_length=100,null=True,blank=True)

class TimetableTable(models.Model):
    Date = models.CharField(max_length=100,null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    hour = models.CharField(max_length=100,null=True,blank=True)
    TEACHERID=models.ForeignKey(TeacherTable,on_delete=models.CASCADE,blank=True,null=True)

class StudentTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    phonenumber = models.BigIntegerField(max_length=100,null=True,blank=True)
    # department = models.CharField(max_length=100,null=True,blank=True)
    DEPARTMENT = models.ForeignKey(DepartmentTable,on_delete=models.CASCADE,null=True,blank=True)



class ReportTable(models.Model):
    STUDENTID=models.ForeignKey(StudentTable,on_delete=models.CASCADE,blank=True,null=True)
    date = models.CharField(max_length=100,null=True,blank=True)
    reply = models.CharField(max_length=100,null=True,blank=True)
    report = models.CharField(max_length=100,null=True,blank=True)


class ComplaintTable(models.Model):
    STUDENTID=models.ForeignKey(StudentTable,on_delete=models.CASCADE,blank=True,null=True)
    date = models.CharField(max_length=100,null=True,blank=True)
    complaint = models.CharField(max_length=100,null=True,blank=True)
    reply = models.CharField(max_length=100,null=True,blank=True)
    report = models.CharField(max_length=100,null=True,blank=True)

class DutyrequestTable(models.Model):
    STUDENTID=models.ForeignKey(StudentTable,on_delete=models.CASCADE,blank=True,null=True)
    department=models.CharField(max_length=100,null=True,blank=True)
    reason=models.CharField(max_length=100,null=True,blank=True)


class Notification_model(models.Model):
    Notification = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True,blank=True)
    updated_at = models.DateField(auto_now=True)




    