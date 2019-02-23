import os
import random
import string
import time
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from registerAPP.models import User


# Create your views here.

class Log:
    def __init__(self,funName):
        self.funObj=funName
    def __call__(self, *args, **kwargs):
        IP=args[0].META["REMOTE_ADDR"]
        UA=args[0].META['HTTP_USER_AGENT']
        with open ('visiterLog.txt','w+') as f:
            f.write(IP+'    '+UA+'   '+time.strftime("%Y-%m-%d %H:%M:%S"))
        return self.funObj(args[0])






@Log
def registerPage(request):
    request.session['a']=122222
    return render(request,"register.HTML")

@Log
def registerChecking(request):
    username=request.POST.get("userid")
    result=User.objects.filter(username=username)
    print(result)
    if result:
        return HttpResponse('exist')
    else:
        return HttpResponse('noexist')

@Log
def registerAction(request):
    try:
        with transaction.atomic():
            username=request.POST.get("userid")
            usrtel=request.POST.get("usrtel")
            email=request.POST.get("email")
            salt=''.join(random.sample(string.ascii_letters+string.digits,4))
            password=make_password(request.POST.get("password"),salt=salt)
            User.objects.create(username=username,password=password,email=email,phone=usrtel)
            return redirect("ShowApp:showMenu")
    except:
        return render(request,'404.html')

