from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):

    context = {}
    if request.method == 'GET':
        return render(request, 'acsys_system/user/login.html')


def signup(request):
    return render(request, 'acsys_system/user/signup.html')
