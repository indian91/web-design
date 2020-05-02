from django.shortcuts import render
from django.http import HttpResponse
from .forms import Signup,Login
from .models import Userinfo
# Create your views here.
def home(request):
    return render(request,'index1.html')
def signup(request):
    form=Signup()
    return render(request,'signup.html',{'form':form})
def aftersignup(request):
    form=Signup(request.POST)
    if form.is_valid():
        username=form.cleaned_data['UserName']
        first_name=form.cleaned_data['Fname']
        last_name=form.cleaned_data['Lname']
        email=form.cleaned_data['Email']
        password=form.cleaned_data['Password']
        s="Your details \n\t\t '{}','{}','{}','{}','{}',".format(username,first_name,last_name,email,password)
        return HttpResponse(s)
def login(request):
    form=Login()
    return render(request,'login.html',{'form':form})