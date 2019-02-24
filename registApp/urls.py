from django.urls import path

from registApp import views

urlpatterns = [
    path('page/',views.registPage,name="page"),
    path('check/',views.registCheck,name="check"),
    path('action/',views.registAction,name="action"),
]