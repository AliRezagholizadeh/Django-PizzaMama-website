from django.shortcuts import render
from django.http import HttpResponse
# # from ..menu.models import Pizza
# # from ..menu.models import Pizza
# from pizzamama.menu.models import Pizza
# from ...pizzamama.menu.models import Pizza
# from .. menu.models import Pizza
# Create your views here.
# from pizzamama.menu.models import Pizza
# from ..menu import Pizza

# import pizzamama.menu.models.Pizza

from Udemy_Course_Django_Heroku.pizzamama.menu.models import Pizza

def index(request):
    pizzas = Pizza.objects.all()
    pizzas_name = [pizza.name for pizza in pizzas]
    pizza_name_str = ','.join(pizzas_name)
    return HttpResponse("Main-page: " + pizza_name_str)



