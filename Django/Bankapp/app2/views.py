# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home2.html')
def index(request):
    return HttpResponse('<h2>This is index page of app2')
