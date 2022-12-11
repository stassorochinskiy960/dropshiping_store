from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


""" 
def shop(request):
    return render(request, 'shop.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
"""

