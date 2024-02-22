
from django.contrib import admin
from django.urls import path
from . views import question_list,question_details,register,create_question,update_question,delete_question,update_answer

urlpatterns = [
    path("", question_list, name = "question-list"),
    path("question/<slug:slug>/",question_details, name = "question-details"),
    path("answer/update/<int:id>/",update_answer, name = "update-answer"),
    path('register/',register,name = "register"),
    path('update/<slug:slug>/',update_question,name = "update-question"),
    path('delete/<slug:slug>/',delete_question,name = "delete-question"),
    path('add/',create_question,name = "add-question"),
]