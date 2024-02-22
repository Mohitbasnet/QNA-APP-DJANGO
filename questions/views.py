from django.shortcuts import render,get_object_or_404,redirect
from . models import Question,Answer
from . forms import UserRegistrationForm,QuestionRegistrationForm,AnswerForm,AnswerUpdateForm,QuestionUpdateForm
# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request,"Qlist.html",{'question_list': question_list})

def question_details(request,slug):
    question = Question.objects.get(slug = slug)
    answer_list = Answer.objects.filter(question = question)

    #ading answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer = form.save()
            return redirect('question-details',slug = slug)
    else:
        form = AnswerForm()
    

    
    return render(request,"Qdetails.html",{"question":question,'answer_list':answer_list,"form":form})

def register(request):

    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            print("new_user:",new_user)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration_done.html',{'user_form': user_form})

    else:
        user_form = UserRegistrationForm()

        
    return render(request,'register.html',{'user_form':user_form})

def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit = False)
            question.author = request.user
            question = question_form.save()
            return redirect('question-list')

    else:
        question_form = QuestionRegistrationForm()

    return render(request, "add_question.html",{"question_form":question_form})

 
def update_question(request,slug):
    question = Question.objects.get(slug = slug)

    form = QuestionUpdateForm(request.POST or None, instance = question)

    if form.is_valid():
        form.save()
        return redirect('question-list')

    return render(request, 'update.html',{'form': form})

def delete_question(request,slug):
    question= Question.objects.get(slug = slug)
    question.delete()
    return redirect('question-list')
def update_answer(request,id):
    answer = Answer.objects.get(id = id)

    form = AnswerUpdateForm(request.POST or None, instance = answer)
    if form.is_valid():
        form.save()
        return redirect('question-details',slug = answer.question.slug)
    return render(request, 'update_answer.html',{'form':form})


def delete_answer(request,id):
    answer = Answer.objects.get(id = id)
    answer.delete()
    return redirect('question-details',slug = answer.question.slug)
    
