# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('developers:login')
    else:
        form = UserCreationForm()
    return render(request,'developers/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("Hi")
            user = form.get_user()
            login(request, user)
            #login the user
            #sleep(300)
    else:
        form = AuthenticationForm()
    return render (request, 'developers/login.html', {'form':form})