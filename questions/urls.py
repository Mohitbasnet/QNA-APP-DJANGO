
from django.contrib import admin
from django.urls import path
from . views import question_list,question_details

urlpatterns = [
    path("question/", question_list, name = "question-list"),
    path("question/<slug:slug>/",question_details, name = "question-details"),
]