from _operator import index

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Professor
from .forms import  ProfessorModelForm
from django.db.models import Avg,Sum,Min,Max,Count
from django.views.generic import View,ListView
from django.http import HttpResponse




# Create your views here.


def Add_Professor(request):

    form = ProfessorModelForm
    student_form = {'form':form}

    if request.method == 'POST':
        Professor_form = ProfessorModelForm(request.POST)
        if Professor_form.is_valid():
            Professor_form.save()
        return Professor_details(request)

    return render(request,'Professor_html/ADD_PROFESSOR.html',student_form)

def Professor_details(request):

    result=Professor.objects.all()

    details={'results':result}
    return render(request,'Professor_html/PROFESSOR_DETAILS.html',details)

def DeleteProfessor(request,id):
    s = Professor.objects.get(id=id)
    s.delete()
    return Professor_details(request)

def UpdateDetails(request,id):
    s = Professor.objects.get(id=id)
    form = ProfessorModelForm(instance=s)
    dict={'form':form}

    if request.method == 'POST':
        student_form = ProfessorModelForm(request.POST,instance=s)
        if student_form.is_valid():
            student_form.save()
        return Professor_details(request)
    return render(request,'Professor_html/UPDATE_PROFESSOR.html',dict)



class firstClassBaseView(View):
    def get(self,request):
        return HttpResponse("<h1>this is class based view</h1>")


from django.shortcuts import render

# Create your views here.
