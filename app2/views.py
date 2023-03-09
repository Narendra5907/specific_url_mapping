from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kohli(request):
    return HttpResponse('<h1><marquee>kohli is the best cricketer in the world</marquee></h1>')
def surya(request):
    return HttpResponse('<h1><marquee>surya is known as sky</marquee></h1>')
