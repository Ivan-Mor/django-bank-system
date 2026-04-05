from django.http import HttpResponse
from django.shortcuts import render

def greeting(request):
    return render(request,'accounts/greeting.html')

# Create your views here.
