from django.shortcuts import render
from django.http import HttpResponse

def mobile(request):
    return HttpResponse("<h1 style='background-color:black;color:burlywood;width:fit-content;padding:10px;border-radius:10px'>My Phone Number is :7987900xxx</h1>")

def mobile1(request):
    return HttpResponse("<h1 style='background-color:black;color:burlywood;width:fit-content;padding:10px;border-radius:10px'>Sagri's Phone Number is :930464xxx</h1>")

def mobile2(request):
    return HttpResponse("<h1 style='background-color:black;color:burlywood;width:fit-content;padding:10px;border-radius:10px'>PC's Phone Number is :88391xxxxx</h1>")

# Create your views here.





