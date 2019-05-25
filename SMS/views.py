from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect
from .models import Person,Student
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from .models import Teacher, Login, Request, Studentsection, Fee
from django.db import connection


# Create your views here.

def index(request):
        
        return render(request, 'SMS/index.html')

def articles(request):
    return render(request, 'SMS/articles.html')

def contact_us(request):
    return render(request, 'SMS/contact-us.html')

def site_map(request):
    return render(request, 'SMS/sitemap.html')

def about(request):
    return render(request, 'SMS/about-us.html')

def login(request):
        incorrect_password = "False"
        if request.method == 'POST':
                print ("logged")
                name = request.POST.get('inputEmail')
                password = request.POST.get('inputPassword')
                print (name)
                print (password)
                if name == "admin@a.com" and password == "1234":
                        return redirect('/admin/')
                else :
                        try :   
                                current_user = Login.objects.get(username = name, password = password)
                                print(current_user.username)
                                if current_user.role == 'Student':
                                        return redirect('/sms/student/' + str(current_user.personid.id) )
                                elif current_user.role == 'Teacher':
                                        return redirect('/sms/teacher/' + str(current_user.personid.id))
                                else:
                                        return redirect('/admin/')
                        except:
                                incorrect_password = "False"
                                return render(request,'sms/login.html', {'incorrectPassword' :incorrect_password})
                
        else:
                return render(request,'sms/login.html', {'incorrectPassword' :incorrect_password})  
        

def view_student_timetable(request,student_id):
    return render(request, 'SMS/TimeTable.html', {'StudentId' : student_id})

def view_student_academic_detail(request, student_id):
        curr_Person = Person.objects.get(id = student_id)
        Name = curr_Person.firstname + " " + curr_Person.lastname
        Email = curr_Person.email
        Contact = curr_Person.contact
        DOB = curr_Person.dateofbirth.strftime('%m/%d/%Y')
        Gender = curr_Person.gender
        if Gender == 1:
                Gender = "Male"
        else :
                Gender = "Female"
                
        curr_Student = Student.objects.get(id = curr_Person)
        RegNo = curr_Student.registrationno
        try : 
                curr_StudentSection = Studentsection.objects.get(studentid = student_id)
                SectionOfStudent = curr_StudentSection.sectionid.name
        except:
                SectionOfStudent = "N/A"
        try:
                TeacherOfStudent = curr_StudentSection.sectionid.teacherid.id.firstname + " " + curr_StudentSection.sectionid.teacherid.id.lastname
        except:
                TeacherOfStudent = "N/A"
        try:
                ClassOfStudent = curr_StudentSection.sectionid.classid.name
                
        except:
              ClassOfStudent = "N/A"
        return render(request, 'SMS/AcademicDetail.html', {'StudentId' : student_id, 'RegNo': RegNo, 'Name' : Name , 'Email' : Email , 'Contact': Contact, 'DOB': DOB, 'Gender': Gender, 'SectionOfStudent' : SectionOfStudent, 'TeacherOfStudent': TeacherOfStudent, 'ClassOfStudent' : ClassOfStudent})

def student(request, student_id):
        curr_Person = Person.objects.get(id = student_id)
        Name = curr_Person.firstname + " " + curr_Person.lastname
        Email = curr_Person.email
        Contact = curr_Person.contact
        DOB = curr_Person.dateofbirth.strftime('%m/%d/%Y')
        Gender = curr_Person.gender
        if Gender == 1:
                Gender = "Male"
        else :
                Gender = "Female"
                
        curr_Student = Student.objects.get(id = curr_Person)
        RegNo = curr_Student.registrationno
        try : 
                curr_StudentSection = Studentsection.objects.get(studentid = student_id)
                SectionOfStudent = curr_StudentSection.sectionid.name
        except:
                SectionOfStudent = "N/A"
        try:
                TeacherOfStudent = curr_StudentSection.sectionid.teacherid.id.firstname + " " + curr_StudentSection.sectionid.teacherid.id.lastname
        except:
                TeacherOfStudent = "N/A"
        try:
                ClassOfStudent = curr_StudentSection.sectionid.classid.name
                
        except:
              ClassOfStudent = "N/A"
        return render(request, 'SMS/AcademicDetail.html', {'StudentId' : student_id, 'RegNo': RegNo, 'Name' : Name , 'Email' : Email , 'Contact': Contact, 'DOB': DOB, 'Gender': Gender, 'SectionOfStudent' : SectionOfStudent, 'TeacherOfStudent': TeacherOfStudent, 'ClassOfStudent' : ClassOfStudent})

def view_date_sheet(request, student_id):
        cursor = connection.cursor()
        result_set = ""
        try:
                cursor.execute('EXEC prDateSheetio @Id ='+ str(student_id) )
                result_set = cursor.fetchall()
        finally:
                cursor.close()  
        print (result_set)
        return render(request, 'SMS/DateSheet.html', {'StudentId' : student_id, 'result' : result_set})

def view_result(request,student_id):
        cursor = connection.cursor()
        result_set = ""
        try:
                cursor.execute('EXEC prStudentResult @Id ='+ str(student_id) )
                result_set = cursor.fetchall()
        finally:
                cursor.close()  
        print (result_set)
        return render(request, 'SMS/Result.html', {'StudentId' : student_id, 'result' : result_set})

def send_student_request(request, student_id):
        if request.method == 'POST':
                Student = Person.objects.get(id = student_id)
                description = request.POST.get('Description')
                if description == None :
                        description = "N/A"
                new_request = Request(personid = Student, description = description)
                new_request.save()
                return render(request, 'SMS/Request.html', {'StudentId' : student_id})
        else:
                return render(request, 'SMS/Request.html', {'StudentId' : student_id})

def upload_student_assignment(request,student_id):
    return render(request, 'SMS/Assignments.html', {'StudentId' : student_id})

def view_student_fee(request, student_id):
        curr_Section = Studentsection.objects.get(studentid = student_id)
        student_class = curr_Section.classid.name
        student_fee = Fee.objects.filter(classid = curr_Section.classid.id).first()
        fee_month = student_fee.month
        challan_id = student_fee.challanid
        due_date = student_fee.duedate.strftime('%m/%d/%Y')
        amount = student_fee.amount

        return render(request, 'SMS/Fee.html', {'StudentId' : student_id, 'Class': student_class, 'Month' : fee_month, 'Id' : challan_id, 'Duedate' : due_date , 'Amount' : amount})


def teacher_dashboard(request,teacher_id):
        
        curr_Person = Person.objects.get(id = teacher_id)
        Name = curr_Person.firstname + " " + curr_Person.lastname
        Email = curr_Person.email
        Contact = curr_Person.contact
        DOB = curr_Person.dateofbirth.strftime('%m/%d/%Y')
        Gender = curr_Person.gender
        if Gender == 1:
                Gender = "Male"
        else :
                Gender = "Female"
        
        curr_Teacher = Teacher.objects.get(id = curr_Person)
        Designation = curr_Teacher.designation
        
        return render(request, 'SMS/indexT.html', {'TeacherId' : teacher_id, 'Name' : Name , 'Email' : Email , 'Contact': Contact, 'DOB': DOB, 'Gender': Gender, 'Designation' : Designation})


def teacher_upload_assignments(request, teacher_id):
        return render(request, 'SMS/AssignmentsT.html', {'TeacherId' : teacher_id})


def teacher_attendance(request,teacher_id):
        return render(request, 'SMS/AttendanceT.html', {'TeacherId' : teacher_id})


def teacher_payroll(request,teacher_id):
        return render(request, 'SMS/payroll.html', {'TeacherId' : teacher_id})


def teacher_request(request,teacher_id):
        if request.method == 'POST':
                description = request.POST.get('Description')
                new_request = Request(personid = 1, description = description)
                new_request.save()
                return render(request, 'SMS/teacher', {'TeacherId' : teacher_id})


        else:
                return render(request, 'SMS/RequestT.html', {'TeacherId' : teacher_id})
        
def teacher_timetable(request,teacher_id):
        return render(request, 'SMS/TimetableT.html', {'TeacherId' : teacher_id})

def teacher_result(request,teacher_id):
        return render(request, 'SMS/ResultT.html', {'TeacherId' : teacher_id})
