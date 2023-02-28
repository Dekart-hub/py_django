from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    cal = models.IntegerField()
    weight = models.IntegerField()
    price = models.IntegerField()


class Dish(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    weight = models.IntegerField()
    products = models.ManyToManyField(Product)


class Cook(models.Model):
    count = models.IntegerField()
    id_dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    prep_date = models.DateTimeField()


