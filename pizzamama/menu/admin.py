from django.contrib import admin
from .models import Pizza
# import .models as md
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'ingredients', 'vegeterian')
    search_fields = ["name", "price", "ingredients", "vegeterian"]


admin.site.register(Pizza, PizzaAdmin)
# admin.site.register(md.Pizza)