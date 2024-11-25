from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sathya(request):
    return HttpResponse('sathya mam  is the HOD of the maths department')