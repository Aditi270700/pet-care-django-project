from django.db import models

# Create your models here.
class Shoping(models.Model):
    name=models.CharField(max_length = 50)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length = 50)
    
    

class Shop(models.Model):
    admin_name = models.CharField(max_length=50)
    admin_email = models.EmailField()
    admin_pass=models.CharField(max_length=50)