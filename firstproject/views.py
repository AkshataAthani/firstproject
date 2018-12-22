from django.http import HttpResponse
from django.shortcuts import render
from . import wordcount

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext= request.GET['fulltext']
    fulltextcount = wordcount.getwordcount(request)
    return render(request, 'count.html', {'fulltext': fulltext, 'fulltextcount':fulltextcount})

def about(request):
     return render (request,'aboutus.html')
