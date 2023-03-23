from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Dish(models.Model):
    name = models.CharField(max_length=256)
    ingridients = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True)
    ccal = models.IntegerField()
    image = models.ImageField(upload_to='dishes/', null=True, blank=True)
    

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    count = models.IntegerField()
    comment = models.CharField(max_length=256, null=True)
    ord_date = models.DateTimeField()
