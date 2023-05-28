from django.shortcuts import render
from django.http import HttpResponse

def render_login(request):
    return render(request, 'login.html')

def login_admin(request):
    return render(request, 'admin.html')


# Create your views here.
