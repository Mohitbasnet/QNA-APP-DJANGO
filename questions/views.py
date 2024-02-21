from django.shortcuts import render,get_object_or_404
from . models import Question
from . forms import UserRegistrationForm
# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request,"Qlist.html",{'question_list': question_list})

def question_details(request,slug):
    question = Question.objects.get(slug = slug)
    return render(request,"Qdetails.html",{"question":question})

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