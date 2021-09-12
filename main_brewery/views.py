from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main_brewery/index.html', {'title': 'Main page', 'tasks': tasks})

def about(request):
    return render(request, 'main_brewery/about.html')

def recipe(request):
    return render(request, 'main_brewery/recipe.html')

def contact(request):
    return render(request, 'main_brewery/contact.html')