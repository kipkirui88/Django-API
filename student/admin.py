from django.contrib import admin

# Register your models here.
from .models import Parent, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'addmission', 'course') 
    

class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'student')   
       
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent ,ParentAdmin)
