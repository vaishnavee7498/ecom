from msilib import Feature

from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from common.forms import UserRegisterForm
from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def sign_up(request):
    reg_form = UserRegisterForm()
    return render(request, 'customer.html', {'reg_form': reg_form})

def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            email = request.POST['email']
            print(email,"email")
            username = request.POST['username']
            password = request.POST['password']
            User.objects.create_user(email=email, username=username, password=password)
            print('user created')
            messages.success(request, 'Your account has been created successfully...')
            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(request.META['HTTP_REFERER'])
    else:
        print(form.errors)
        messages.error(request, 'Username may already exist or must be atleast 8-10 characters long & '
                                'Password must be 8 characters long')
        return redirect(request.META['HTTP_REFERER'])

class LoginView(View):
    template_name = 'customer.html'
    success_url = 'common/product'

    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(self.success_url)
            else:
                messages.info(request, 'invalid username or password')
                return redirect("/")
        else:
            return render(request, self.template_name)
            # return redirect(request.META['HTTP_REFERER'])


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('login')


from django.shortcuts import render
from .models import *

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})