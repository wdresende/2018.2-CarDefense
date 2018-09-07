from django.db import models


class User(models.Model):
    car_model = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    car_plate = models.SlugField(max_length=8)
    