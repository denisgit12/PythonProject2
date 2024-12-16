from django.db import models

class PizzaModel(models.Model):
    class Meta:
        db_table = 'pizzas'

    name = models.CharField(max_length=30)
    size = models.IntegerField()
    price = models.FloatField()
