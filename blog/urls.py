from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello',helloworld),
    path('stu',numberofstudent),
    path('quo',quotes),
]
