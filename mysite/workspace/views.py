from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# if the user is not logged in, he will be redirected to the login page
# @login_required(login_url='/workspace/login/')
def render_login(request):
    # rendering of the login.html site
    return render(request, 'login.html')

def login_admin(request):
    return render(request, 'admin.html')


# renders the signup.html file, if requested
def render_signup(request):
    return render(request, 'signup.html')