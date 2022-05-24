from django.shortcuts import render


def login(request):
    return render(request, 'home.html')

def LoginView(request):
    return render(request, 'products.html')
