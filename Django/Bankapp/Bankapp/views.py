from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')
def index(request):
    return HttpResponse('<h2>This is index page of project</h2>')
    
