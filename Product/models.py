from django.db import models


class Product(models.Model):
    
    name = models.CharField()
    
    price = models.FloatField()
    
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    



class Category(models.Model):
    
    name = models.CharField()
    


