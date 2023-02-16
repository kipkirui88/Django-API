from tabnanny import verbose
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    addmission = models.IntegerField()
    course = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Student'
    
class Parent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Parent'