from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Classes, Section
from .models import Person, Student, Teacher, Request, Fee, Salary,Classcourses, Datesheet, Studentsection, Courses, Login, Result


admin.site.site_header = 'School Management System'

class StudentAdmin(admin.StackedInline):
    model = Student
class PersonAdmin(admin.ModelAdmin):
    
    inlines = [StudentAdmin]


admin.site.register(Person,PersonAdmin)


class SectionAdmin(admin.StackedInline):
    model = Section
    
class ClassAdmin(admin.ModelAdmin):
    inlines = [SectionAdmin]

admin.site.register(Classes,ClassAdmin)


class RequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Request,RequestAdmin)

class FeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fee,FeeAdmin)

class SalaryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Salary,SalaryAdmin)

class DatesheetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Datesheet,DatesheetAdmin)

class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Classcourses,CourseAdmin)

class StudentsectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Studentsection,StudentsectionAdmin)

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Courses,CourseAdmin)

class LoginAdmin(admin.ModelAdmin):
    pass
admin.site.register(Login,LoginAdmin)


class ResultAdmin(admin.ModelAdmin):
    pass
admin.site.register(Result,ResultAdmin)














"""
class myClassAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}
    change_form_template = 'adminApp/changeClass.html'
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        print(object_id)
        depId = Class.objects.get(pk=object_id).DepartmentId
        extra_context['osm_data'] = Section.objects.filter(
            ClassId=object_id, DepartmentId=depId)
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

        """