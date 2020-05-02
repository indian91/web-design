from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello World to Django</h1>')
def index(request):
    return render(request,'index.html')