from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

# Create your views here.
def hello(request):
    return HttpResponse("Hello world! This is SERWeb project!")


