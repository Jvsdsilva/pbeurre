from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Create tables database
class Category(models.Model):
    idCategory = models.CharField(max_length=200)
    nameCategory = models.CharField(max_length=200)

    def __str__(self):
        return self.nameCategory


class Store(models.Model):
    idStore = models.CharField(max_length=200)
    nameStore = models.CharField(max_length=200)

    def __str__(self):
        return self.nameStore


class Products(models.Model):
    nameAlim = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    descriptionAlim = models.CharField(max_length=3000)
    nutritionGrade = models.CharField(max_length=200)
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    idStore = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameAlim


class Foodsave(models.Model):
    idAliment = models.ForeignKey(Products, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
