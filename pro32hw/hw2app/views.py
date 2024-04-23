from django.shortcuts import render
from django.http import HttpResponse

def pramod(request):
    return HttpResponse("I am elder son")

def praveen(request):
    return HttpResponse("I am younger son")

def trsinha(request):
    return HttpResponse("My DAD")

def ksinha(request):
    return HttpResponse("My MOM")

def pratikkunj(request):
    return HttpResponse("My HOUSE Name")
# Create your views here.

