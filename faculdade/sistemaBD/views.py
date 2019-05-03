from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'sistemaBD/index.html')

def cursos(request):
    return render(request,'sistemaBD/cursos.html')

def noticias(request):
    return render(request,'sistemaBD/noticias.html')

#{% load staticfiles %}
#<link href="{% static "css/estilo.css" %}" rel="stylesheet">
