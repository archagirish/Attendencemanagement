import datetime
import os
import time
import cv2
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
import face_recognition

from myapp.serializer import *

from .forms import *

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        try:
            username=request.POST['username']
            password=request.POST['password']
            login_obj=LoginTable.objects.get(username=username,password=password)
            if login_obj.type=="admin":
                return HttpResponse('''<script>alert("Welcome to adminhome" );window.location="dashboard/"</script>''')
            elif login_obj.type=="teacher":
                request.session['LOGINID']=login_obj.id
                return HttpResponse('''<script>alert("Welcome to Teacherhome" );window.location="teacher_dashboard/"</script>''')
        except:
             return HttpResponse('''<script>alert("Invalid username or password" );window.location="/"</script>''')

class Logout(View):
    def get(self, request):
        return HttpResponse('''<script>alert("logout successfully");window.location="/"</script>''')
        
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
        obj=ClassTable.objects.all()
        return render(request,'administrator/student.html', {'val': obj})    
    
    def post(self,request):
        c=Adduser_form(request.POST, request.FILES)
        class_no = request.POST['class_no']

        if c.is_valid():
            f=c.save(commit=False)
            f.LOGINID=LoginTable.objects.create(username=request.POST['username'],password=request.POST['password'], type="student")
            f.CLASS=ClassTable.objects.get(id=class_no)
            f.save()
            return redirect('/manage_student')
        

class Editstudent(View):
    def get(self,request,pk):
        c=StudentTable.objects.get(pk=pk) 
        val=ClassTable.objects.all()
        return render(request,'administrator/edit_student.html', {'b':c,'val':val}) 
    
    def post(self,request,pk):
        c=StudentTable.objects.get(pk=pk)
        d=Adduser_form(request.POST,instance=c)
        if d.is_valid():
            f=d.save(commit=False)
            class_no=request.POST['class_no']
            f.CLASS=ClassTable.objects.get(id=class_no)
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

class select_class_staff(View):
    def get(self,request):
        obj = ClassTable.objects.all()
        return render(request, "teacher/select_class.html", {'obj': obj})  


class manage_timetable(View):
    def post(self, request):
        class_id=request.POST['class_id']
        request.session['class_id']=class_id
        class_obj = ClassTable.objects.get(id=class_id)
        subjects = SubjectTable.objects.filter(DEPARTMENT_id=class_obj.DEPARTMENT.id)
        existing_days = Timetable1.objects.filter(CLASS_id=class_obj).values_list('day', flat=True)
        all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        available_days = [day for day in all_days if day not in existing_days]
        return render(request, 'teacher/manage_timetable.html', {
            'subjects': subjects,
            'available_days': available_days
        })
    
class add_timetable_action(View):
    def post(self, request):
        day = request.POST['day']
        slot_9_10 = request.POST['slot_9_10']
        slot_10_11 = request.POST['slot_10_11']
        slot_11_12 = request.POST['slot_11_12']
        slot_1_2 = request.POST['slot_1_2']
        slot_2_3 = request.POST['slot_2_3']
        slot_3_4 = request.POST['slot_3_4']
        obj = Timetable1()
        obj.CLASS=ClassTable.objects.get(id=request.session['class_id'])
        obj.day=day
        obj.slot_9_10=SubjectTable.objects.get(id=slot_9_10)
        obj.slot_10_11=SubjectTable.objects.get(id=slot_10_11)
        obj.slot_11_12=SubjectTable.objects.get(id=slot_11_12)
        obj.slot_1_2=SubjectTable.objects.get(id=slot_1_2)
        obj.slot_2_3=SubjectTable.objects.get(id=slot_2_3)
        obj.slot_3_4=SubjectTable.objects.get(id=slot_3_4)
        obj.save()
        return HttpResponse('''<script>alert("successfully added");window.location="/select_class_staff#about"</script>''')

class select_class_staff1(View):
    def get(self,request):
        obj = ClassTable.objects.all()
        return render(request, "teacher/select_class1.html", {'obj': obj})
    
class view_timetable(View):
    def post(self, request):
        class_id=request.POST['class_id']
        # Query all timetable entries from the database
        timetable_entries = Timetable1.objects.filter(CLASS_id=class_id).order_by('day')
        # Render the timetable in a template
        return render(request, 'teacher/timetable.html', {'timetable_entries': timetable_entries})    


class view_attendace_staff(View):
    def get(self, request):
        # Fetch all classes for the dropdown
        classes = ClassTable.objects.all()
        return render(request, 'teacher/select_class_attend.html', {'obj': classes})
    def post(self, request):
        if request.method == 'POST':
            class_id = request.POST.get('class_id')
            date = request.POST.get('date')

            # Get students in the selected class
            students = StudentTable.objects.filter(CLASS_id=class_id)
            
            # Fetch attendance for the selected date and class
            attendance_data = []
            for student in students:
                student_attendance = AttendanceTable.objects.filter(
                    STUDENT_ID=student, Date=date
                ).order_by('Period')
                attendance_record = {
                    'student': student,
                    'attendance': {att.Period: att.Attendance for att in student_attendance},
                }
                attendance_data.append(attendance_record)
            
            return render(request, 'teacher/show_attendance.html', {
                'attendance_data': attendance_data,
                'date': date,
            })
        
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
         class_id=request.POST['class_id']
         request.session['class_id']=class_id
         class_obj = ClassTable.objects.get(id=class_id)
         subjects = SubjectTable.objects.filter(DEPARTMENT_id=class_obj.department.id)
         existing_days = Timetable1.objects.filter(CLASS_id=class_obj).values_list('day', flat=True)
         all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
         available_days = [day for day in all_days if day not in existing_days]
         return render(request, 'teacher/manage_timetable.html', {
        'subjects': subjects,
        'available_days': available_days
        })
    
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
    

class select_slot(View):
      def get(self, request):
         return render(request, 'teacher/view_slots.html')

class take_attendance(View):
    def post(self, request):
        slot = request.POST['slot']
        print("---------------->Camera started")
        name_list=[]
                    
        # Path to the known images folder and the text file with names
        known_images_path = "C:\\Users\\LENOVO\\Desktop\\archa\\face_recog\\Face_recog\\media\\known_images"
        names_file = "C:\\Users\\LENOVO\\Desktop\\archa\\face_recog\\Face_recog\\media\\known_faces.txt"

        # Function to load names from the text file
        def load_names(names_file):
            with open(names_file, "r") as f:
                names = [line.strip() for line in f.readlines()]
            return names

        # Load known face names from the text file
        person_names = load_names(names_file)
        known_face_encodings = []
        known_face_names = []

        # Loop through each person folder inside known_images
        for i, person_folder in enumerate(os.listdir(known_images_path)):
            person_folder_path = os.path.join(known_images_path, person_folder)
            person_name = person_names[i]  # Fetch name corresponding to the person folder
            
            # Loop through each image in the person's folder
            for image_file in os.listdir(person_folder_path):
                image_path = os.path.join(person_folder_path, image_file)
                image = face_recognition.load_image_file(image_path)
                
                # Encode the face and store it with the person's name
                face_encoding = face_recognition.face_encodings(image)
                if face_encoding:
                    known_face_encodings.append(face_encoding[0])
                    known_face_names.append(person_name)
                    print(f"Encoded {image_file} for {person_name}")
                else:
                    print(f"No face found in {image_file}, skipping")

        # Final check for any mismatches
        print(f"Number of encodings: {len(known_face_encodings)}, Number of names: {len(known_face_names)}")

        # Start capturing video from the webcam
        cap = cv2.VideoCapture(0)
        check_flag=0
        while check_flag==0:
            start_time = time.time()
            while time.time() - start_time < 5:
                ret, frame = cap.read()
                cv2.imshow("Real-time Face Recognition", frame)
                cv2.waitKey(1)
            cv2.imwrite("imageeee.jpg",frame)
            cap.release()
            cv2.destroyAllWindows()

            frame = cv2.imread("imageeee.jpg")

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get face encodings for each face in the frame
            face_encodings = face_recognition.face_encodings(rgb_frame)

            for face_encoding in face_encodings:
                name = "Unknown"

                # Compare the face encodings with known faces
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                if True in matches:
                    match_index = matches.index(True)
                    if match_index < len(known_face_names):
                        name = int(known_face_names[match_index])
                        print(type(name))
                        name_list.append(name)
                        print(name_list)
                        check_flag=1
                    else:
                        print(f"Error: match_index {match_index} out of range")
                        
            if name_list:
                
                current_time = datetime.now() 
                print("----------->", current_time)
                
                for i in name_list:
                    obj = AttendanceTable()
                    obj.Date=current_time
                    obj.Attendance="Present"
                    obj.Period = slot
                    obj.STUDENT_ID=Student.objects.get(id=i)
                    obj.save()
                return HttpResponse('''<script>alert("Done");window.location="/staff_home#about"</script>''')
            else:
                return HttpResponse('''<script>alert("No Faces");window.location="/staff_home#about"</script>''')
            

class Leave(View):
      def get(self, request):
         obj=DutyrequestTable.objects.all()
         return render(request, 'teacher/leave.html',{'a':obj})

            
class accept_leave(View):
      def get(self, request, r_id):
        obj=DutyrequestTable.objects.get(id=r_id)
        obj.status='accept'
        obj.save()
        return HttpResponse('''<script>alert("accept leave");window.location="/leave#about"</script>''')

class reject_leave(View):
      def get(self, request, r_id):
        obj=DutyrequestTable.objects.get(id=r_id)
        obj.status='reject'
        obj.save()
        return HttpResponse('''<script>alert("reject leave");window.location="/leave#about"</script>''')

            
            
# //////////////////////////////////////////////////// API ////////////////////////////////////////////////

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

class LoginPageApi(APIView):
    def post(self, request):
        response_dict= {}
        password = request.data.get("password")
        print("Password ------------------> ",password)
        username = request.data.get("username")
        print("Username ------------------> ",username)
        try:
            user = LoginTable.objects.filter(username=username, password=password).first()
            print("user_obj :-----------", user)
        except LoginTable.DoesNotExist:
            response_dict["message"] = "No account found for this username. Please signup."
            return Response(response_dict, status.HTTP_200_OK)
      
        if user.type == "student":
            response_dict = {
                "login_id": str(user.id),
                "user_type": user.type,
                "status": "success",
            }   
            print("User details :--------------> ",response_dict)
            return Response(response_dict, status.HTTP_200_OK)
        else:
            response_dict["message "] = "Your account has not been approved yet or you are a CLIENT user."
            return Response(response_dict, status.HTTP_200_OK)




class StudentReg(APIView):
    def get(self, request):
        # Query all departments
        departments = DepartmentTable.objects.all()
        # Serialize the department data
        serializer = DepartmentSerializer(departments, many=True)
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        """
        Handle student registration.
        """
        print("###############", request.data)
        
        # Serialize user and login data
        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)
        
        # Validate the serializers
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            print("&&&&&&&&&&&&&&&&& Data is valid")
            
            # Save login and user data
            password = request.data['Password']
            department = request.data['department']
            obj = DepartmentTable.objects.get(id=department)
            login_profile = login_serial.save(Type='student', Password=password)
            user_serial.save(LOGIN=login_profile, DEPARTMENT=obj)
            
            # Respond with the serialized user data
            return Response(user_serial.data, status=status.HTTP_201_CREATED)

        # Log detailed errors for debugging
        print("User Serializer Errors:", user_serial.errors)
        print("Login Serializer Errors:", login_serial.errors)

        # Return validation errors
        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)


class ViewTimeTable(APIView):
    def get(self, request,lid):
        obj = StudentTable.objects.get(LOGINID_id=lid)
        obj1 = Timetable1.objects.filter(CLASS_id=obj.CLASS.id)
        serializer = TimetableSerializer(obj1, many = True)
        print("time----------------> ", serializer)
        return Response(serializer.data)


class ViewAttendanceApi(APIView):
    def get(self, request, lid):
        obj = AttendanceTable.objects.filter(STUDENT_ID__LOGINID_id=lid)
        serializer = AttendanceSerializer(obj, many = True)
        print("time----------------> ", serializer)
        return Response(serializer.data)

class ViewProfileApi(APIView):
    def get(self, request, lid):
        obj = StudentTable.objects.filter(LOGINID_id=lid)
        serializer = UserSerializer(obj, many = True)
        print("time----------------> ", serializer)
        return Response(serializer.data)

class NotificationApi(APIView):
    def get(self, request):
        obj = Notification.objects.all()
        serializer = NotificationSerializer(obj, many = True)
        print("time----------------> ", serializer)
        return Response(serializer.data)

class SendComplaintApi(APIView):
    def get(self, request, lid):
        obj = Complaint.objects.filter(STUDENT__LOGIN_id=lid)
        print("%%%%%%%%%%%%%%",obj)
        complaint_serializer = ComplaintSerializer(obj, many=True)
        return Response(complaint_serializer.data)
    def post(self, request,lid):
        comp_serializer = SendComplaintSerializer(data=request.data)
        user_obj = Student.objects.get(LOGIN_id=lid)
        if comp_serializer.is_valid():
            comp_serializer.save(STUDENT=user_obj, reply="pending")
            return Response(comp_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comp_serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        


