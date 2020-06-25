from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'acsys_system/user/login.html')


def signin(request):
    return render(request, 'acsys_system/user/signin.html')
