from django.contrib.auth.hashers import check_password
from django.shortcuts import render,HttpResponse

# Create your views here.
from login_app.models import User


def login_page(request):
    return  render(request,'login.html')

def login_logic(request):
    req_ip = request.get_host()
    req_url = request.path
    print(req_ip,req_url)
    username = request.POST.get('username')
    inputpassword = request.POST.get('password')
    try:
        user = User.objects.get(username = username)
    except:
        return HttpResponse({'ERROR',})
    password = user.password
    if check_password(inputpassword,password):
        request.session['flag'] = username
        return HttpResponse('OK')
    return HttpResponse('ERROR')
