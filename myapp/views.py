from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import *

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']
        login_obj=LoginTable.objects.get(username=username,password=password)
        if login_obj.type=="admin":
            return HttpResponse('''<script>alert("Welcome to adminhome" );window.location="dashboard/"</script>''')
        # elif login_obj.type=="teacher":
        
class dashboard(View):
    def get(self, request):
        return render(request, 'admin/admin_dashboard.html')




class Pass(View):
    def get(self,request):
        return render(request, 'changepass.html')
    
class Notification(View):
    def get(self,request):
        return render(request, 'admin/notification.html')
    def post(self,requet):
        c=Notification_form(requet.POST)
        if c.is_valid():
            c.save()
            return redirect('managenotification')

    
# class Notifi(View):
#     def get(self,request):
#         return render(request, 'admin/notification.html')
#     def post(self,request):
#         c = Add_notification(request.POST)
#         if c.is_valid():
#             c.save()
#             return redirect('managenotification')
        
# ///////////////////////////////////////////// ADMIN ///////////////////////////////////////////

class Course(View):
    def get(self, request):
        obj=DepartmentTable.objects.all()
        return render(request, 'admin/add_cousce.html',{'val': obj})
    def post(self,request):
        c=Course_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('manage_couse')
    
class Deletecourse(View):
     def get(self,request,pk):
        e=CourseTable.objects.get(pk=pk)
        e.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/manage_couse/"</script>''')

class Editcourse (View):
     def get(self,request, pk):
        c=CourseTable.objects.get(pk=pk)
        return render(request,'admin/edit_course.html', {'a':c})
     
     def post(self,request,pk):
        c=CourseTable.objects.get(pk=pk)
        d=Course_form(request.POST,instance=c)
        if d.is_valid():
            d.save()
            return redirect('manage_couse')

 

    
class Dept(View):
    def get(self, request):
        return render(request, 'admin/adddept.html')
    def post(self,request):
        c=Department_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('manage_dept')
    
class Complaint(View):
    def get(self,request):
        return render(request, 'admin/complaint.html') 

class Editcomp(View):
    def get(self,request):
        return render(request,'admin/edit_complaint.html')

class Editnotification(View):
    def get(self,request):
        return render(request,'admin/edit_notification.html')  

class Managecomp(View):
    def get(self,request):
        return render(request,'admin/manage_complaint.html') 
    
class Managecourse(View):
    def get(self,request):
        obj=CourseTable.objects.all()
        return render(request,'admin/manage_couse.html',{'a':obj})
    
class Managedept(View):
    def get(self,request):
        e=DepartmentTable.objects.all()
        return render(request,'admin/manage_dept.html', {'a':e})

class Deletedept(View):
    def get(self,request,pk):
        e=DepartmentTable.objects.get(pk=pk)
        e.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/manage_dept/"</script>''')

class Editdept(View):
    def get(self,request,pk):
        e=DepartmentTable.objects.get(pk=pk)
        return render(request,'admin/edit_dept.html',{'a':e})
    
    def post(self,request,pk):
        c=DepartmentTable.objects.get(pk=pk)
        d=Department_form(request.POST,instance=c)
        if d.is_valid():
            d.save()
            return redirect('manage_dept')
    
class Managenotification(View):
    def get(self,request):
        obj=Notification_model.objects.all()
        return render(request,'admin/managenotification.html', {'a':obj})
    
class Deletenotification(View):
    def get(self,request,pk):
        c=Notification_model.objects.get(pk=pk)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/managenotification/"</script>''')
    
class Editnotification(View):
    def get(self,request,pk):
        c=Notification_model.objects.get(pk=pk) 
        return render(request,'admin/edit_notification.html', {'b':c}) 
    
    def post(self,request,pk):
        c=Notification_model.objects.get(pk=pk)
        d=Notification_form(request.POST,instance=c)
        if d.is_valid():
            d.save()
            return redirect('managenotification')
        
    
class Managestudent(View):
    def get(self,request):
        obj=StudentTable.objects.all()
        return render(request,'admin/managestudent.html', {'a':obj})
    
class Manageteacher(View):
    def get(self,request):
        return render(request,'admin/manageteacher.html')
    
class Student(View):
    def get(self,request):
        obj=DepartmentTable.objects.all()
        return render(request,'admin/student.html', {'val': obj})    
    
    def post(self,request):
        c=Adduser_form(request.POST)
        if c.is_valid():
            f=c.save(commit=False)
            f.LOGINID=LoginTable.objects.create(username=request.POST['username'],password=request.POST['password'], type="student")
            f.save()
            return redirect('/manage_student')
        

class Editstudent(View):
    def get(self,request,pk):
        c=StudentTable.objects.get(pk=pk) 
        return render(request,'admin/edit_student.html', {'b':c}) 
    
    def post(self,request,pk):
        c=StudentTable.objects.get(pk=pk)
        d=Adduser_form(request.POST,instance=c)
        if d.is_valid():
            d.save()
            return redirect('manage_student')

class Deletestudent(View):
    def get(self,request,pk):
        c=StudentTable.objects.get(pk=pk)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/manage_student/"</script>''')

   
class Teacher(View):
    def get(self,request):
        return render(request,'admin/teacher.html')
    




# ///////////////////////////////////////////// TEACHER ///////////////////////////////////////////


class Add_report(View):
    def get(self,request):
        return render(request,'teacher/add_report.html')
    
class Edit_profile(View):
    def get(self,request):
        return render(request,'teacher/edit_profile.html')
    
class Edit_report(View):
    def get(self,request):
        return render(request,'teacher/edit_report.html')
    
class  Manage_attendence(View):
    def get(self,request):
        return render(request,'teacher/manage_attendance.html')
    
class Manage_report(View):
    def get(self,request):
        return render(request,'teacher/Manage_report.html')

class Manage_subjectallocated(View):
    def get(self,request):
        return render(request,'teacher/manage_subjectallocated.html')
    
class Manage_timtable(View):
    def get(self,request):
        return render(request,'teacher/manage_timtable.html')
    
class  Manageprofile(View):
    def get(self,request):
        return render(request,'teacher/mangeprofile.html')
    
class Profile(View):
    def get(self,request):
        return render(request,'teacher/profile.html')
    
class View_staff(View):
    def get(self,request):
        return render(request,'teacher/view_staff.html')
    
class View_student(View):
    def get(self,request):
        return render(request,'teacher/view_student.html')
    
class Viewnotification(View):
    def get(self,request):
        return render(request,'teacher/viewnotification.html')

    

        
