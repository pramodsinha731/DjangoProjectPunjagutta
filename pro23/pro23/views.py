from django.http import HttpResponse

def v1(request):
    data="<h1 style='color:red'>Hello</h1>"
    return HttpResponse(data)

def v2(request):
    data="<h2>How are you ?</h2>"
    return HttpResponse(data)

def v3(request):
    data="<h2>How are you doing ?</h2>"
    return HttpResponse(data)

def v4(request):
    data="<h2>I am fine , thank you</h2>"
    return HttpResponse(data)

def v5(request):
    data="<h2>I am doing great !!</h2>"
    return HttpResponse(data)

def v6(request):
    data="<h2>Nice to meet you</h2>"
    return HttpResponse(data)