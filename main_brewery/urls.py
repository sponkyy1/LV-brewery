from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('recipe', views.recipe),
    path('contact', views.contact),
]