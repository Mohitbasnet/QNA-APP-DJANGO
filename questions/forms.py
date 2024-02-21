from django import forms
from django.contrib.auth import get_user_model
from . models import Question,Answer
from django.forms import ModelForm
User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password doesn't match")

            return cd['password2']

class QuestionRegistrationForm(ModelForm):
    class Meta:
        model = Question
        fields = ('title','body')


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)