from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def saludo(request):
    return HttpResponse("Hola buenas noches")