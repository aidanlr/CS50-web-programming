from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name: str):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })