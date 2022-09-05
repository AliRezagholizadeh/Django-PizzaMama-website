from django.db import models

# Create your models here.


class Orders(models.Model):
    current_time = models.CharField(max_length= 20)
    current_date = models.CharField(max_length= 40)
    n_order = models.IntegerField(default= 0)

    def __str__(self):
        return self.n_order