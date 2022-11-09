# chat/views.py
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from channels.auth import get_user

from .models import *





def room(request):
    username = request.GET.get('username', 'Anonymous')
    return render(request, 'theme/room.html')


  
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('forum')
    return render(request, 'theme/login.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        if username and password :
            user = User.objects.create_user(username=username,password=password)
            if user:
                return redirect('login')
    return render(request,'theme/register.html')

def Logout(request):
    user = get_user()
    if user is not None:
        logout(request)
        return redirect('login')

def chat_room(request, label):
    room, created = MyRoom.objects.get_or_create(label=label)

    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, 'theme/myroom.html', {'room': room, 'messages': messages})
    