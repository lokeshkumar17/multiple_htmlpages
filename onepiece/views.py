from django.shortcuts import render
from django.http import HttpResponse

def zoro(request):
    return render(request,'zoro.html')

def luffy(request):
    return HttpResponse('<h1>Gear 5th</h1>')

# Create your views here.
