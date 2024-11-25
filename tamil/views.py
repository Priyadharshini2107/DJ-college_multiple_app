from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def suresh(request):
    return HttpResponse('suresh sir is the HOD of the tamil department')