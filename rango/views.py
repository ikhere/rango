from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Rango home page"""
    context = {'boldmessage': 'SERIOUSLY!!'}
    return render(request, 'rango/index.html', context)


def about(request):
    """Information about rango"""
    context = {'message': 'about'}
    return render(request, 'rango/about.html', context)
