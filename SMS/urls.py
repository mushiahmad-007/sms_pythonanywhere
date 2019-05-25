from django.urls import path

from . import views

app_name = 'SMS'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='About'),
    path('student/<int:student_id>/', views.student, name = 'student'),
    path('articles/', views.articles, name = 'Articles'),
    path('contact_us/', views.contact_us, name = 'Contact_Us'),
    path('sitemaps/', views.site_map, name = 'Sitemaps'),
    path('login/', views.login , name = 'Login'),
    path('student/<int:student_id>/timetable/', views.view_student_timetable, name ='ViewTimeTableSudent'),
    path('student/<int:student_id>/AcademicDetail/', views.view_student_academic_detail, name = 'StudentAcademicDetail'),
    path('student/<int:student_id>/ViewDateSheet/' , views.view_date_sheet ,name = 'ViewDateSheet'),
    path('student/<int:student_id>/ViewResult/' , views.view_result ,name = 'ViewResult'),
    path('student/<int:student_id>/SendStudentRequest/' , views.send_student_request ,name = 'SendStudentRequest'),
    path('student/<int:student_id>/UploadStudentAssignment/' , views.upload_student_assignment ,name = 'UploadStudentAssignment'),
    path('student/<int:student_id>/ViewStudentFee/' , views.view_student_fee ,name = 'ViewStudentFee'),

    path('teacher/<int:teacher_id>/', views.teacher_dashboard, name = 'Teacher'),
    path('teacher/<int:teacher_id>/timetabe/', views.teacher_timetable, name = 'TeacherTimeTable'),
    path('teacher/<int:teacher_id>/assignments/', views.teacher_upload_assignments, name = 'TeacherAssignments'),
    path('teacher/<int:teacher_id>/attendance/', views.teacher_attendance, name = 'TeacherAttendance'),
    path('teacher/<int:teacher_id>/payroll/', views.teacher_payroll, name = 'TeacherPayroll'),
    path('teacher/<int:teacher_id>/request/', views.teacher_request, name = 'TeacherRequest'),
    path('teacher/<int:teacher_id>/result/', views.teacher_result, name = 'TeacherResult'),
    path('GeneratePDF/', views.GeneratePDF, name = 'FeeChallan'),
]