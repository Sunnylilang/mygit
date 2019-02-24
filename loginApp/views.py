from django.contrib.auth.hashers import check_password
from django.shortcuts import render,HttpResponse

# Create your views here.
from loginApp.models import User


def loginPage(request):
    return  render(request,'login.html')

def loginAction(request):
    username = request.POST.get('username')
    inputpassword = request.POST.get('password')
    print(1)
    try:
        user = User.objects.get(username = username)
    except:
        return HttpResponse({'ERROR',})
    password = user.password
    if check_password(inputpassword,password):
        request.session['flag'] = username
        return HttpResponse('OK')
    print('hehe')
    return HttpResponse('ERROR')
