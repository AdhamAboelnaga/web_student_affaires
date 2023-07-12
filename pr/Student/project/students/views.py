from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Student
from Home import *
# Create your views here.


@login_required(login_url='page1')
def indexAdd(request):
    return render(request, 'student/indexAdd.html')


@login_required(login_url='page1')
def indexDept(request):
    x = Student.objects.filter(Department='IT').values() | Student.objects.filter(Department='CS').values() | Student.objects.filter(
        Department='IS').values() | Student.objects.filter(Department='AI').values() | Student.objects.filter(Department='DS').values()
    return render(request, 'student/indexDept.html', {'stu': x})


@login_required(login_url='page1')
def indexSearch(request):
    x = Student.objects.filter(status='Active').values()
    return render(request, 'student/indexSearch.html', {'stu': x})


@login_required(login_url='page1')
def indexView(request):
    x = Student.objects.all()
    return render(request, 'student/indexView.html', {'stu': x})


@login_required(login_url='page1')
def indexUpdate(request):
    return render(request, 'student/Edit.html')


@login_required(login_url='page1')
def indexStudentAdd(request):
    x = Student.objects.all()
    if request.method == "POST":
        name = request.POST.get('username')
        Id = request.POST.get('id')
        Data_of_birth = request.POST.get('date_of_birth')
        Department = request.POST.get('department')
        Email = request.POST.get('email')
        Phone = request.POST.get('mobile_number')
        Gpa = request.POST.get('gpa')
        Level = request.POST.get('level')
        Gender = request.POST.get('gender')
        Status = request.POST.get('status')
        for a in x:
            if Id == a.id:
                messages.warning(request, 'This id used before, enter valid one')
                return redirect('add')

        for a in x:
            if Email == a.Email:
                messages.warning(request, 'please enter valid email')
                return redirect('add')

        y = len(Id)
        if y != 8:
            print(y)
            messages.warning(request, 'please enter correct id!')
            return redirect('add')
        if Level == '1':
            if Department != 'General':
                messages.warning(request, 'please enter correct Level and  Department!')
                return redirect('add')
        if Level == '2':
            if Department != 'General':
                messages.warning(
                    request, 'please enter correct Level and  Department!')
                return redirect('add')
        if Level == '3':
            if Department == 'General':
                messages.warning(request, 'please enter correct Level and  Department!')
                return redirect('add')
        if Level == '4':
            if Department == 'General':
                messages.warning(request, 'please enter correct Level and  Department!')
                return redirect('add')

        data = Student(Name=name, id=Id, Date_of_birth=Data_of_birth, Department=Department,
                       Email=Email, MobileNumber=Phone, GPA=Gpa, level=Level, Gender=Gender, status=Status)
        data.save()
        print('complete add student')
        return render(request, 'Home/indexHome.html')
    else:
        print('Error method')
        return redirect('add')


@login_required(login_url='page1')
def deleted(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('dept'))


@login_required(login_url='page1')
def deleteg(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('search'))


@login_required(login_url='page1')
def deletev(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('view'))


@login_required(login_url='page1')
def EditStudent(request, Id):
    display = Student.objects.get(id=Id)
    return render(request, 'student/Edit.html', {'student': display})


@login_required(login_url='page1')
def UpdateStudent(request, Id):
    if request.method == "POST":
        updateStuden = Student.objects.get(id=Id)
        updateStuden.Name = request.POST.get('username')
        updateStuden.id = request.POST.get('id')
        updateStuden.Date_of_birth = request.POST.get('date_of_birth')
        updateStuden.Department = request.POST.get('Department')
        updateStuden.Email = request.POST.get('email')
        updateStuden.MobileNumber = request.POST.get('mobile_number')
        updateStuden.GPA = request.POST.get('gpa')
        updateStuden.level = request.POST.get('level')
        updateStuden.Gender = request.POST.get('gender')
        updateStuden.status = request.POST.get('status')
        updateStuden.save()
        return render(request, 'Home/indexHome.html')
