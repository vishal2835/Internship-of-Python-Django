from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def homepageview(request):
    return HttpResponse("<h1>welocome to homepage</h1>")

def aboutpageview(request):
    return HttpResponse("<h1>about us page</h1>")

def contactpageview(request):
    return HttpResponse("<h1>contact us page</h1>")

