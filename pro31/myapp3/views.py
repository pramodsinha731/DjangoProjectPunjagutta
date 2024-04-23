from django.shortcuts import render
from django.http import HttpResponse

def pincode(request):
    return HttpResponse("<h1 style='background-color:black;color:burlywood;width:400px;border-radius:10px'>493111</h1>")

def pincode1(request):
    return HttpResponse("<h1 style='background-color:black;color:burlywood;width:400px;border-radius:10px'>493000</h1>")

def pincode2(request):
    return HttpResponse("<h1 style='background-color:black;color:burlywood;width:400px;border-radius:10px'>500082</h1>")
# Create your views here.
