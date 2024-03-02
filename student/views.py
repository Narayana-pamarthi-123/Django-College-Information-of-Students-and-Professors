from _operator import index

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Student
from .forms import  StudentModelForm
from django.db.models import Avg,Sum,Min,Max,Count
from django.views.generic import View,ListView
from django.http import HttpResponse




# Create your views here.

@login_required(login_url="/login/")
def Add_Student(request):

    form = StudentModelForm
    student_form = {'form':form}

    if request.method == 'POST':
        student_form = StudentModelForm(request.POST)
        if student_form.is_valid():
            student_form.save()
        return Student_details(request)

    return render(request,'student_html/ADD_STUDENT.html',student_form)

def Student_details(request):

    result=Student.objects.all()

    details={'results':result}
    return render(request,'student_html/STUDENTS_DETAILS.html',details)

def DeleteStudent(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return Student_details(request)

def UpdateDetails(request,id):
    s = Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict={'form':form}

    if request.method == 'POST':
        student_form = StudentModelForm(request.POST,instance=s)
        if student_form.is_valid():
            student_form.save()
        return Student_details(request)
    return render(request,'student_html/update_student.html',dict)



class firstClassBaseView(View):
    def get(self,request):
        return HttpResponse("<h1>this is class based view</h1>")


