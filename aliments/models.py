from django.db import models


# Create your models here.
class Category(models.Model):
    idCategory = models.CharField(max_length=200)
    nameCategory = models.CharField(max_length=200)
    
    def __str__(self):
        return self.idCategory

class Store(models.Model):
    idStore = models.CharField(max_length=200)
    nameStore = models.CharField(max_length=200)
    
    def __str__(self):
        return self.idStore

class Products(models.Model):
    nameAlim = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    descriptionAlim = models.CharField(max_length=1500)
    nutritionGrade = models.CharField(max_length=200)
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    idStore = models.ForeignKey(Store, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nameAlim

class User(models.Model):
    nameUser = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.nameUser


class Foodsave(models.Model):
    idAliment = models.ForeignKey(Products, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.idAliment


