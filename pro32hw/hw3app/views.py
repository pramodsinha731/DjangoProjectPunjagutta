from django.shortcuts import render
from django.http import HttpResponse

def Kashi_Sir(request):
    return HttpResponse("Teaches Python")

def Afroz_Sir(request):
    return HttpResponse("Teaches SQL")

def Ningraj_Sir(request):
    return HttpResponse("Teaches Web-Tech")

def Vivek_Sir(request):
    return HttpResponse("Teaches Java")

def Geeta_Mam(request):
    return HttpResponse("Teaches React")



# Create your views here.
