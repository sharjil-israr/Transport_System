from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    if request.user.is_anonymous:
       return redirect('login')
    else:
       return redirect('dashboard')    
