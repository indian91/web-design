from django.db import models

# Create your models here.
class Userinfo(models.Model):
    UserName=models.CharField(max_length=100,unique=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.CharField(max_length=100)
    