from django.urls import path
from captchaAPP import views

urlpatterns = [
    path('getCaptcha/',views.getCaptcha,name="getCaptcha"),
    path('checkCaptcha/',views.checkCaptcha,name="captchaChecking"),
]