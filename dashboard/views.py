from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def new(request):
    return render(request, 'dashboard/new.html')

def assets(request):
    return render(request, 'dashboard/assets.html')

def maintainance(request):
    return render(request, 'dashboard/maintainance.html')