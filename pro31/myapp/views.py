from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='color:red'>This is Home Page</h1>")

# Create your views here.
