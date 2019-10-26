from django.db import models


# Create your models here.
class Category(models.Model):
    idCategory = models.CharField(max_length=200)
    nameCategory = models.CharField(max_length=200)
    
    def __str__(self):
<<<<<<< HEAD
        return self.nameCategory

=======
        return self.idCategory
>>>>>>> 692f9a37d206bfd5a751bacd9f152ef07dece708

class Store(models.Model):
    idStore = models.CharField(max_length=200)
    nameStore = models.CharField(max_length=200)
    
    def __str__(self):
<<<<<<< HEAD
        return self.nameStore

=======
        return self.idStore
>>>>>>> 692f9a37d206bfd5a751bacd9f152ef07dece708

class Products(models.Model):
    nameAlim = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
<<<<<<< HEAD
    descriptionAlim = models.CharField(max_length=3000)
=======
    descriptionAlim = models.CharField(max_length=1500)
>>>>>>> 692f9a37d206bfd5a751bacd9f152ef07dece708
    nutritionGrade = models.CharField(max_length=200)
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    idStore = models.ForeignKey(Store, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nameAlim

<<<<<<< HEAD

=======
>>>>>>> 692f9a37d206bfd5a751bacd9f152ef07dece708
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


