from django.urls import path

from registerAPP import views

urlpatterns = [
    path('registerPage/',views.registerPage,name="registerPage"),
    path('registerChecking/',views.registerChecking,name="registerChecking"),
    path('registerAction/',views.registerAction,name="registerAction"),
]