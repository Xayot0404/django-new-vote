from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import ListView
from .models import *


def index(request):

    questions = School.objects.all()
    

    context = {
        "questions": questions
    }

    return render(request, 'index.html',context)

def Menu(request, question_id):
    if request.POST:
        son = request.POST["ovoz"]
        savoll = menus.objects.get(id=son)
        savoll.ovozlar_soni += 1
        savoll.save()
    menu = menus.objects.filter(school_id=question_id)
    questions = School.objects.get(id=question_id)
    context = {
        "menu": menu,
        "questions": questions
    }
    return render(request,'main.html',context)






# class SchooLView(ListView):
#     model = School
#     template_name = 'index.html'


# class MenusView(ListView):
#     model = menus
#     template_name = 'main.html'