from django.shortcuts import render,get_object_or_404
from . models import Question
# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request,"Qlist.html",{'question_list': question_list})

def question_details(request,slug):
    question = Question.objects.get(slug = slug)
    return render(request,"Qdetails.html",{"question":question})
