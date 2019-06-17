from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import logout

def login_facebook(request):
    return render(request, "login_social.html")

def home(request):
    return render(request, "index_facebook.html")


def logout_view(request):
    logout(request)
    return redirect(login_facebook)