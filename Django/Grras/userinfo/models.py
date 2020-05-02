from django.db import models

# Create your models here.
class Users(models.Model):
    UserName=models.CharField(label='UserName',max_length=100,unique=True)
    Fname=models.CharField(label='FirstName',max_length=20)
    Lname=models.CharField(label='LastName',max_length=20,required=False)
    Email=models.EmailField(label='Email',max_length=60)
    pic=models.ImageField(label='Image')
    Password=models.CharField(label='Password',max_length=100)
    def __str__(self):
        return self.UserName