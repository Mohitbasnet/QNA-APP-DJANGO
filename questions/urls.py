
from django.contrib import admin
from django.urls import path
from . views import question_list

urlpatterns = [
    path("question/", question_list, name = "question-list"),
]