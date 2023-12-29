from django.db import models

# Create your models here.
class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    head_of_department = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=70)
    akts = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="classes")

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    classes = models.ManyToManyField(Class,  null=True, blank=True)
