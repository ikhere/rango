from django.shortcuts import render
from rango.models import Category


def index(request):
    """Rango home page"""
    category_list = Category.objects.order_by('-likes')[:5]
    context = {'categories': category_list}
    return render(request, 'rango/index.html', context)


def about(request):
    """Information about rango"""
    context = {'message': 'about'}
    return render(request, 'rango/about.html', context)
