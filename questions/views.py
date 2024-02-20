from django.shortcuts import render
from . models import Question
# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request,"Qlist.html",{'question_list': question_list})