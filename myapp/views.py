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
        elif login_obj.type=="teacher":
            request.session['LOGINID']=login_obj.id
            return HttpResponse('''<script>alert("Welcome to Teacherhome" );window.location="teacher_dashboard/"</script>''')
class Logout(View):
    def get(self, request):
        return render(request,'login.html')
        
class dashboard(View):
    def get(self, request):
                # Count total students, teachers, departments, and complaints
        total_students = StudentTable.objects.count()
        total_teachers = TeacherTable.objects.count()
        total_departments = DepartmentTable.objects.count()
        total_complaints = ComplaintTable.objects.count()
        
        # Pass these counts as context to the template
        context = {
            'total_students': total_students,
            'total_teachers': total_teachers,
            'total_departments': total_departments,
            'total_complaints': total_complaints
        }
        
        return render(request, 'administrator/admin_dashboard.html',context)




class Pass(View):
    def get(self,request):
        return render(request, 'changepass.html')
    
class Notification(View):
    def get(self,request):
        return render(request, 'administrator/notification.html')
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
        return render(request, 'administrator/add_cousce.html',{'val': obj})
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
        return render(request,'administrator/edit_course.html', {'a':c})
     
     def post(self,request,pk):
        c=CourseTable.objects.get(pk=pk)
        d=Course_form(request.POST,instance=c)
        if d.is_valid():
            d.save()
            return redirect('manage_couse')

 

    
class Dept(View):
    def get(self, request):
        return render(request, 'administrator/adddept.html')
    def post(self,request):
        c=Department_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('manage_dept')
    
class Complaint(View):
   def get(self, request):
        obj=ComplaintTable.objects.all()
        return render(request, 'administrator/add_complaint.html',{'val': obj})
   def post(self,request):
        c=Complaint_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('manage_complaint')

class Editcomp(View):
    def get(self,request):
        return render(request,'administrator/edit_complaint.html')
    
class Deletecomp(View):
     def get(self,request,pk):
        e=ComplaintTable.objects.get(pk=pk)
        e.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/manage_complaint/"</script>''')    

class Editnotification(View):
    def get(self,request):
        return render(request,'administrator/edit_notification.html')  

class Managecomp(View):
    def get(self,request):
        obj=ComplaintTable.objects.all()
        return render(request,'administrator/manage_complaint.html',{'val':obj}) 
    
class Managecourse(View):
    def get(self,request):
        obj=CourseTable.objects.all()
        return render(request,'administrator/manage_couse.html',{'a':obj})
    
class Managedept(View):
    def get(self,request):
        e=DepartmentTable.objects.all()
        return render(request,'administrator/manage_dept.html', {'a':e})

class Deletedept(View):
    def get(self,request,pk):
        e=DepartmentTable.objects.get(pk=pk)
        e.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/manage_dept/"</script>''')

class Editdept(View):
    def get(self,request,pk):
        e=DepartmentTable.objects.get(pk=pk)
        return render(request,'administrator/edit_dept.html',{'a':e})
    
    def post(self,request,pk):
        c=DepartmentTable.objects.get(pk=pk)
        d=Department_form(request.POST,instance=c)
        if d.is_valid():
            d.save()
            return redirect('manage_dept')
    
class Managenotification(View):
    def get(self,request):
        obj=Notification_model.objects.all()
        return render(request,'administrator/managenotification.html', {'a':obj})
    
class Deletenotification(View):
    def get(self,request,pk):
        c=Notification_model.objects.get(pk=pk)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/managenotification/"</script>''')
    
class Editnotification(View):
    def get(self,request,pk):
        c=Notification_model.objects.get(pk=pk) 
        return render(request,'administrator/edit_notification.html', {'b':c}) 
    
    def post(self,request,pk):
        c=Notification_model.objects.get(pk=pk)
        d=Notification_form(request.POST,instance=c)
        if d.is_valid():
            d.save()
            return redirect('managenotification')
        
    
class Managestudent(View):
    def get(self,request):
        obj=StudentTable.objects.all()
        return render(request,'administrator/managestudent.html', {'a':obj})
    
class Manageteacher(View):
    def get(self,request):
        obj=TeacherTable.objects.all()
        return render(request,'administrator/manageteachers.html',{'a':obj})
    
class Editteacher(View):
    def get(self,request,pk):
         c=TeacherTable.objects.get(pk=pk) 
         val=DepartmentTable.objects.all()
         return render(request,'administrator/editteacher.html', {'b':c,'val':val}) 
        
    def post(self,request,pk):
        c=TeacherTable.objects.get(pk=pk)
        d=Teacher_form(request.POST,instance=c)
        if d.is_valid():
            f=d.save(commit=False)
            department=request.POST['department']
            f.DEPARTMENT=DepartmentTable.objects.get(id=department)
            f.save()
            return redirect('/manage_teacher')
        
class Deleteteacher(View):
    def get(self,request,pk):
        c=LoginTable.objects.get(pk=pk)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/manage_teacher/"</script>''')


  
class Student(View):
    def get(self,request):
        obj=DepartmentTable.objects.all()
        return render(request,'administrator/student.html', {'val': obj})    
    
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
        val=DepartmentTable.objects.all()
        return render(request,'administrator/edit_student.html', {'b':c,'val':val}) 
    
    def post(self,request,pk):
        c=StudentTable.objects.get(pk=pk)
        d=Adduser_form(request.POST,instance=c)
        if d.is_valid():
            f=d.save(commit=False)
            department=request.POST['department']
            f.DEPARTMENT=DepartmentTable.objects.get(id=department)
            f.save()
            d.save()
            return redirect('manage_student')

class Deletestudent(View):
    def get(self,request,pk):
        c=StudentTable.objects.get(pk=pk)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/manage_student/"</script>''')

   
class Teacher(View):
    def get(self,request):
        obj=DepartmentTable.objects.all()
        return render(request,'administrator/teacher.html', {'val': obj})
    
    def post(self,request):
        c=Teacher_form(request.POST)
        usernme = request.POST['username']
        password = request.POST['password']
        try:
            LoginTable.objects.get(username=usernme)
            return HttpResponse('''<script>alert("username already exist");window.location="/manage_teacher"</script>''')
        except LoginTable.DoesNotExist:
            if c.is_valid():
                f=c.save(commit=False)
                f.LOGINID=LoginTable.objects.create(username=request.POST['username'],password=request.POST['password'], type="teacher")
                # department=request.POST['department']
                # f.DEPARTMENT=DepartmentTable.objects.get(id=department)
                f.save()
                return redirect('/manage_teacher')
            
class Subject(View):
    def get(self,request):
        obj=DepartmentTable.objects.all()
        return render(request,'administrator/subject.html',{'val': obj})
    def post(self,request):
        c=Subject_form(request.POST)
        if c.is_valid():
            f=c.save(commit=False)
            departmentid=request.POST['DEPARTMENT']
            obj=DepartmentTable.objects.get(id=departmentid)
            f.DEPARTMENT=obj
            f.save()
            return redirect('/managesubject')
        
class Managesubject(View):
    def get(self,request):
        dept=DepartmentTable.objects.all()
        obj=SubjectTable.objects.all()
        return render(request,'administrator/manage_subject.html',{'a':obj, 'b':dept})
    
class search_subject(View):
    def get(self,request):
        dept_id = request.POST['dept']
        dept=DepartmentTable.objects.all()
        print("$$$$$$$$$$$$$$", dept)
        obj=SubjectTable.objects.filter(DEPARTMENT_id=dept_id)
        return render(request,'administrator/manage_subject.html',{'a':obj, 'b':dept})
            
    def post(self,request):
        dept_id = request.POST['dept']
        print("$$$$$$$$$$$$$$", dept_id)
        obj=SubjectTable.objects.filter(DEPARTMENT_id=dept_id)
        return render(request,'administrator/manage_subject.html',{'a':obj})
            
class Deletesubject(View):
    def get(self,request,pk):
        c=SubjectTable.objects.get(pk=pk)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/dashboard/"</script>''')
    
class Editsubject(View):
    def get(self,request,pk):
        c=SubjectTable.objects.get(pk=pk) 
        val=DepartmentTable.objects.all()
        return render(request,'administrator/edit_subject.html', {'b':c,'val':val}) 
    
    def post(self,request,pk):
        c=SubjectTable.objects.get(pk=pk)
        d=Adduser_form(request.POST,instance=c)
        if d.is_valid():
            f=d.save(commit=False)
            department=request.POST['department']
            f.DEPARTMENT=DepartmentTable.objects.get(id=department)
            f.save()
            d.save()
            return redirect('manage_subject')
    
class reply(View):
    def get(self,request,pk):
        c=ComplaintTable.objects.get(pk=pk)
        print(c)
        return render(request,'administrator/complaint.html',{'c':c})
    
    def post(self,requet,pk):
        reply=requet.POST['reply']
        obj=ComplaintTable.objects.get(pk=pk)
        obj.reply=reply
        obj.save()
        return HttpResponse('''<script>alert("reply sent successfully");window.location="/manage_complaint"</script>''')

# ///////////////////////////////////////////// TEACHER ///////////////////////////////////////////

class Teacher_dashboard(View):
    def get(self,request):
        return render(request,'teacher/teacher_dashboard.html')
    
    
class Add_report(View):
    def get(self, request):
        obj=ReportTable.objects.all()
        return render(request, 'teacher/add_report.html',{'val': obj})
    def post(self,request):
        c=Addreport(request.POST)
        if c.is_valid():
            c.save()
            return redirect('manage_report')
          
class Edit_profile(View):
    def get(self,request):
        obj = TeacherTable.objects.get(LOGINID_id=request.session['LOGINID'])
        return render(request,'teacher/edit_profile.html',{'a':obj})
    
class Edit_report(View):
    def get(self,request):
        return render(request,'teacher/edit_report.html')
    
class Attendance(View):
    def get(self, request):
        obj=AttendanceTable.objects.all()
        return render(request, 'teacher/add_complaint.html',{'val': obj})
    def post(self,request):
        c=Complaint_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('manage_complaint')
    
    
class  Manage_attendence(View):
    def get(self,request):
        obj=AttendanceTable.objects.all()
        return render(request,'teacher/manage_attendance.html',{'val':obj})
    
    
class Manage_report(View):
    def get(self,request):
        return render(request,'teacher/Manage_report.html')

class Manage_subjectallocated(View):
    def get(self,request):
        obj=SubjectallocatedTable.objects.all()
        return render(request,'teacher/manage_subjectallocated.html',{'val':obj} )
    
class Manage_timtable(View):
    def get(self,request):
        obj=TimetableTable.objects.all()
        return render(request,'teacher/manage_timtable.html',{'val':obj})
    
class  Manageprofile(View):
    def get(self,request):
        return render(request,'teacher/mangeprofile.html')
    
class Profile(View):
    def get(self,request):
        return render(request,'teacher/profile.html')
    
class View_staff(View):
    def get(self,request):
        obj=StaffTable.objects.all()
        return render(request,'teacher/view_staff.html',{'val':obj})
    
class View_student(View):
    def get(self,request):
        return render(request,'teacher/view_student.html')
    
class Viewnotification(View):
    def get(self,request):
        return render(request,'teacher/viewnotification.html')


    

     



        
