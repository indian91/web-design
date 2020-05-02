from django.shortcuts import render
from django.http import HttpResponse
from . forms import Signup,Login
def index(request):
    return render(request,'index1.html')
def signup(request):
    form=Signup()
    return render(request,'signup.html',{'form':form})
def login(request):
    form=Login()
    return render(request,'login.html',{'form':form})
def afterlogin(request):
    form=Login(request.POST)
    if form.is_valid():
        username=form.cleaned_data['UserName']
        password=form.cleaned_data['Password']
        s=f'Hello {username} with {password}'
        return HttpResponse(s)
    else:
        msg='Form is not in valid Form'
        return render('login.html',{'msg':msg})