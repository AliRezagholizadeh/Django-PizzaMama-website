from django.db import models

# Create your models here.

class Pizza (models.Model):
    name = models.CharField(max_length= 200)
    price = models.FloatField(default=0)
    ingredients = models.CharField(max_length= 500)
    vegeterian = models.BooleanField(default=False)


# class Meal(models.Model):
#     name;
#     ingredients;
#     splitted_workload;
