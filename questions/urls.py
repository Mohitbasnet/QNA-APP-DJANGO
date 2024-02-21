
from django.contrib import admin
from django.urls import path
from . views import question_list,question_details,register,create_question

urlpatterns = [
    path("", question_list, name = "question-list"),
    path("question/<slug:slug>/",question_details, name = "question-details"),
    path('register/',register,name = "register"),
    path('addquestion/',create_question,name = "add-question"),
]