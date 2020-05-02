from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
def home(request):
    return render(request,'home1.html')
def index(request):
    new_user=Users.objects.create(UserName='deepscool001',FirstName='Chintu',LastName='Singh',Email='deepscool01@gmail.com',Password='chintu@123')
    new_user.save()
    return HttpResponse('<h1>User Created Successfully.........</h1>')
    


