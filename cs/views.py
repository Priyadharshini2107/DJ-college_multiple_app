from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def janani(request):
    return HttpResponse('janani mam  is the HOD of the computer science department')
