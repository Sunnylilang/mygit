from django.urls import path
from captchaApp import views

urlpatterns = [
    path('getCaptcha/',views.getCaptcha,name="getCaptcha"),
    path('checkCaptcha/',views.checkCaptcha,name="checkCaptcha"),
]