
from django.contrib import admin
from django.urls import path
from . views import question_list,question_details,register,create_question,update_question,delete_question,update_answer,delete_answer,change_profile,list_info

urlpatterns = [
    path("", question_list, name = "question-list"),
    path("question/<slug:slug>/",question_details, name = "question-details"),

    path('register/',register,name = "register"),
    path('update/<slug:slug>/',update_question,name = "update-question"),
    path('delete/<slug:slug>/',delete_question,name = "delete-question"),
    path('add/',create_question,name = "add-question"),
    path("answer/update/<int:id>/",update_answer, name = "update-answer"),
    path("answer/delete/<int:id>/",delete_answer, name = "delete-answer"),
    path('profile/',change_profile,name = "change-profile"),
    path('list/',list_info,name = 'list'),



]