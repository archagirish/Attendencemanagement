from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
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
        
class Class(View):
    def get(self, request):
         obj=ClassTable.objects.all()
         return render(request, 'administrator/manage_class.html',{'val': obj})
class Addclass(View):
    def get(self, request):
        obj=DepartmentTable.objects.all()
        return render(request, 'administrator/addclass.html',{'val': obj})
    def post(self,request):
        class_no = request.POST.get('ClassNo')
        department = request.POST.get('department')
        print("###############", department)
        dept_obj = DepartmentTable.objects.get(id=department)
        obj = ClassTable()
        obj.ClassNo=class_no
        obj.DEPARTMENT=dept_obj
        obj.save()
        return HttpResponse('''<script>alert("added successfully");window.location="/manage_class"</script>''')

class delete_class(View):
    def get(self, request, pk):
        obj = ClassTable.objects.get(id=pk)
        obj.delete()
        return HttpResponse('''<script>alert("added successfully");window.location="/manage_class"</script>''')
    
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

class Timetable(View):
    def get(self,request,cls,sem):
        obj=SubjectTable.objects.all()
        a=TeacherTable.objects.all()
        print("aaaaaaaaaaaaaaaaaaaaaaa",obj)
        print("##########################")
        print("fffffffffffffffffffffffffff",a)
        return render(request,'administrator/Timetable.html',{'cls':cls,'sem':sem})   
    def post(self, request):
        print("hhhhhhhhhhhhhhhhhhhhh")
        c = TimeTable_form(request.POST)
        cls=request.POST['CLASS']
        sem=request.POST['sem']
        if c.is_valid():
            c.save()
            redirect_url = reverse('Timetableview', kwargs={'cls': cls, 'sem': sem})
        
            return HttpResponse(f'''<script>alert("Time Table added successfully");window.location="{redirect_url}"</script>''')

class Timetableview(View):
    def get(self,request,cls,sem):
        obj=SubjectTable.objects.all()
        a=TeacherTable.objects.all()
        classno=ClassTable.objects.get(id=cls)
        obj=SubjectTable.objects.all()
        a=TeacherTable.objects.all()
        print("aaaaaaaaaaaaaaaaaaaaaaa",obj)
        print("##########################")
        print("fffffffffffffffffffffffffff",a)
        
        # Fetch timetable data for the given class and semester
        timetable = TimetableTable.objects.filter(CLASS=classno, sem=sem)

        # Organize timetable data into a dictionary
        schedule = {}
        for entry in timetable:
            if entry.Day not in schedule:
                schedule[entry.Day] = {}
            schedule[entry.Day][entry.hour] = entry
        context = {
            'classno': classno,
            'sem': sem,
            'val': obj,
            'c': a,
            'schedule': schedule,
            'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            'periods': ['1', '2', '3', '4', '5'],
        }


        return render(request,'administrator/Timetable.html',context)   
 
    
class Dept_sem(View):
    def get(self,request):
        obj=ClassTable.objects.all()
        return render(request,'administrator/Dept_Sem.html',{'val':obj})
    def post(self,request):
        classno = request.POST['classno']
        print(classno)
        classno=ClassTable.objects.get(id=classno)
        obj=SubjectTable.objects.all()
        a=TeacherTable.objects.all()
        print(classno)
        sem = request.POST['sem']
        print(sem)
        # request.session['subj'] = classno
        # request.session['sem'] = sem
        # print("##############", request.session['subj'], request.session['sem'])
        timetable = TimetableTable.objects.filter(CLASS=classno, sem=sem)
                # Prepare the schedule as a dictionary
        print(timetable)
        schedule = {}
        for entry in timetable:
            if entry.Day not in schedule:
                schedule[entry.Day] = {}
            schedule[entry.Day][entry.hour] = entry

        print(schedule)
        context = {
            'classno': classno,
            'sem': sem,
            'val': obj,
            'c': a,
            'schedule': schedule,
            'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            'periods': ['1', '2', '3', '4', '5'],
        }

        return render(request,'administrator/Timetable.html',context)



            
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
        obj=TimetableTable.objects.all()
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
        obj=TeacherTable.objects.all()
        print('oooooooooooooooo',obj)
        return render(request,'teacher/view_staff.html',{'a':obj})
    
class View_student(View):
    def get(self,request):
        obj=StudentTable.objects.all()
        return render(request,'teacher/view_student.html',{'a':obj})
    
class Viewnotification(View):
    def get(self,request):
        obj=Notification_model.objects.all()
        return render(request,'teacher/viewnotification.html',{'a':obj})


    

     



        
