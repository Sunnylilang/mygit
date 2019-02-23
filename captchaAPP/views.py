import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import random,string
from captcha.image import ImageCaptcha

def getCaptcha(request):
    img = ImageCaptcha()
    code=random.sample(string.ascii_uppercase+string.ascii_lowercase+string.digits,4)
    random_code=''.join(code)
    print(random_code)
    request.session['code'] = random_code
    data=img.generate(random_code)#生成图片
    return HttpResponse(data,"image/png")

def checkCaptcha(request):
    try:
        code=request.session.get('code')
        yourCode=request.GET.get('yourcode')
        print(yourCode)
        print(code)
        if code.lower()==yourCode.lower():
            print("right")
            return HttpResponse('right')
        return HttpResponse('wrong')
    except:
        return HttpResponse('wrong')