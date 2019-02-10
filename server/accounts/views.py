from django.shortcuts import render, HttpResponseRedirect
from accounts.forms import AccountUserLoginForm
from django.contrib import auth
from django.urls import reverse

# Create your views here.

def login(request):
    title = 'вход'

    login_form = AccountUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    content = {'title': title, 'login_form': login_form}
    return render(request, 'accounts/login.html', content)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')