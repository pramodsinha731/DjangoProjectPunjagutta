from django.shortcuts import render
from django.http import HttpResponse

def samsung(request):
    return HttpResponse("<h1>Samsung Galaxy S24 Ultra</h1>")
def oneplus(request):
    return HttpResponse("<h1>One Plus 12R</h1>")
def iphone(request):
    return HttpResponse("<h1>Iphone 15 pro max</h1>")
def oppo(request):
    return HttpResponse("<h1>Oppo Reno 2F</h1>")
def iqoo(request):
    return HttpResponse("<h1>iQOO 12</h1>")

# Create your views here.
