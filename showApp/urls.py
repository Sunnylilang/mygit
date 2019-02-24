from django.urls import path

from showApp import views

urlpatterns = [
    path('data/',views.showData,name='data'),
    path('introduce/',views.showIntroduce,name='introduce'),
    path('main/',views.showMain,name='main'),
    path('keywordQuery/',views.keywordQuery,name="keywordQuery"),
    path('brokenLine/',views.brokenLine,name="brokenLine"),
    path('broken/',views.showBrokenline,name="broken")
]