from django.shortcuts import render
from rango.models import Category
from rango.models import Page


def index(request):
    """Rango home page"""
    category_list = Category.objects.order_by('-likes')[:5]
    context = {'categories': category_list}
    return render(request, 'rango/index.html', context)


def about(request):
    """Information about rango"""
    context = {'message': 'about'}
    return render(request, 'rango/about.html', context)


def category(request, category_name_slug):
    """Details about category"""
    context = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context['pages'] = pages
        context['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context)
