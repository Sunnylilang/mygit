from django.urls import path

from ShowApp import views

app_name = 'ShowApp'
urlpatterns = [
    path('showData/',views.showMain,name='showData'),
    path('showIntroduce/',views.showIntroduce,name='showIntroduce'),
    path('showMenu/',views.showData,name='showMenu'),
    path('keywordQuery/',views.keywordQuery,name="keywordQuery"),
    path('brokenLine/',views.brokenLine,name="brokenLine"),
    path('showBroken/',views.showBrokenline,name="showBroken")
]