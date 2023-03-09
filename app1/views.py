from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<h1>dhoni is the best finisher in the world</h1>')
def Rohit(request):
    return HttpResponse('<h1>Rohit is a best opner</h1>')