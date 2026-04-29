from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, 'blog/home.html')

def About(request):
    return render(request, 'blog/about.html')
