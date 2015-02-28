from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = render(request,'index.htm')
    return response