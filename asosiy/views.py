from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages


def register(request):
    if request.method == 'POST' and request.POST.get('p')==request.POST.get('p2'):
        User.objects.create_user(
            username = request.POSt.get('l'),
            password = request.POSt.get('p'),
        )
        return redirect("login")
    return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['l'],
            password = request.POST['p']
        )
        if user is None:
            return redirect('login')
        login(request,user)
        return redirect("/maqolalar/")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect("/")

def maqolalar(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            Maqola.objects.create(
                sarlavha = request.POST['s'],
                mavzu = request.POST['mv'],
                matn = request.POST['mt'],
                muallif = Muallif.objects.get(user= request.user)
            )
            return redirect("/maqolalar/")
        content = {
            'maqolalar':Maqola.objects.filter(muallif__user=request.user)
        }
        return render(request,'maqola.html',content)
    return redirect("/")

def maqola(request,son):
    if request.user.is_authenticated:
        content = {
            'maqola' : Maqola.objects.get(id=son)
        }
        return render(request,'bitta_maqola.html',content)