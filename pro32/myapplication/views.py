from django.shortcuts import render
from django.http import HttpResponse

def p1(request):
    return HttpResponse("Hello")

def p2(request):
    return HttpResponse("Hi")
# Create your views here.
