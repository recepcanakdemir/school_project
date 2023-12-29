from django.shortcuts import render,redirect
from django.http import JsonResponse
from . models import Student, School, Department, Teacher,Class
# Create your views here.

def index(request):
    students = Student.objects.all()
    classes = Class.objects.all()
    return render(request, "school/index.html",{
        "students": students
    })

def ogrenci_ekle(request):
    if request.method=="POST":
        first_name = request.POST.get('fname') 
        last_name = request.POST.get('soyad') 
        email = request.POST.get('email')
        department_name = request.POST.get('department')
        classes = request.POST.get('classes') 
        department = Department.objects.all().filter(department_name = department_name).first()
        new_student=Student.objects.create(
            first_name =  first_name,
            last_name = last_name,
            email = email,
            department = department,
        )
        new_student.classes.set(classes)
        new_student.save()
        return redirect('index')
    classes = Class.objects.all()
    departments = Department.objects.all()
    return render(request, "school/ogrenci_ekle.html",{
        "classes":classes,
        "departments":departments
    })

def ogrenci_ekle(request):
    if request.method=="POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('soyad')
        email = request.POST.get('email')
        department_name = request.POST.get('department')
        classes_selected = request.POST.getlist('classes')

        # Get the Department instance
        department = Department.objects.get(department_name=department_name)

        # Create a new student instance
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            department=department
        )

        # Add selected classes to the student
        for class_name in classes_selected:
            class_instance = Class.objects.get(class_name=class_name)
            student.classes.add(class_instance)

        return redirect('index')  # Redirect to the desired URL after creating the student
    classes = Class.objects.all()
    departments = Department.objects.all()
    return render(request, "school/ogrenci_ekle.html",{
        "classes":classes,
        "departments":departments
    })

def sil(request, student_id):
    Student.objects.all().filter(student_id=student_id).delete()
    return redirect('index')

def edit(request, student_id):
    student = Student.objects.get(student_id=student_id)
    classes = Class.objects.all()
    departments = Department.objects.all()

    if request.method == "POST":
        # Diğer alanları aldığınız gibi sınıf alanını da alın
        first_name = request.POST.get('fname')
        last_name = request.POST.get('soyad')
        email = request.POST.get('email')
        department_name = request.POST.get('department')
        classes_selected = request.POST.getlist('classes')

        # Seçili sınıfları temizleyin
        student.classes.clear()

        # Yeni seçili sınıfları ekleyin
        for class_name in classes_selected:
            class_instance = Class.objects.get(class_name=class_name)
            student.classes.add(class_instance)

        student.first_name = first_name
        student.last_name = last_name
        student.email = email
        student.department = Department.objects.get(department_name=department_name)
        student.save()

        return redirect('index')

    return render(request, "school/edit.html", {
        "student": student,
        "classes": classes,
        "departments": departments,
    })
