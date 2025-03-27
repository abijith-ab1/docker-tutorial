from django.shortcuts import render, redirect
from .tasks import *

def home_view(request):
    return render(request, 'home.html')

def count_to_10(request):
    count_task.delay()
    return redirect('home')