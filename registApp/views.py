import os
import random
import string
import time
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from loginApp.models import User


# Create your views here.


def registPage(request):
    return render(request,"register.HTML")


def registCheck(request):
    username=request.POST.get("userid")
    result=User.objects.filter(username=username)
    if result:
        return HttpResponse('exist')
    else:
        return HttpResponse('noexist')


def registAction(request):
    try:
        with transaction.atomic():
            username=request.POST.get("userid")
            usrtel=request.POST.get("usrtel")
            email=request.POST.get("email")
            password=make_password(request.POST.get("password"))
            User.objects.create(username=username,password=password,email=email,phone=usrtel)
            return redirect("show:main")
    except:
        return render(request,'404.html')

