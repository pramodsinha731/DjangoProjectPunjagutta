from django.shortcuts import render
from django.http import HttpResponse

def address(request):
    return HttpResponse("<h1 style='background-color:black;color:burlywood;width:400px;border-radius:10px'>Raipur , Chhattishgarh</h1>")

def address1(request):
    return HttpResponse("<h1 style='background-color:black;color:burlywood;width:400px;border-radius:10px'>Sapphire Greens , Raipur</h1>")

def address2(request):
    return HttpResponse("<h1 style='background-color:black;color:burlywood;width:400px;border-radius:10px'>Punjagutta , Telangana</h1>")

# Create your views here.
