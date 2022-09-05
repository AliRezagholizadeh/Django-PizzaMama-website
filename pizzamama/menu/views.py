from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.

def index(request):
    pizzas = Pizza.objects.all()
    pizzas_name = [pizza.name for pizza in pizzas]
    return HttpResponse(f"Hi, This is a pizza menu page.{str(pizzas_name)}")