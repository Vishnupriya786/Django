from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def createHome(request):
    return HttpResponse ("Hello world!!!");
