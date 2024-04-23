from django.shortcuts import render
from django.http import HttpResponse

def sher(request):
    return HttpResponse("Vinayak is sher")

def suar(request):
    return HttpResponse("HAI NA !!")

def pc(request):
    return HttpResponse("OH Ha !!")

def krk(request):
    return HttpResponse("Acha Ji")

def chorha(request):
    return HttpResponse("Jiotune")

# Create your views here.
