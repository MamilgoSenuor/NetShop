from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hi! This is a internet shop")