#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 9:52
# @Author  : lilang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from loginApp import views

urlpatterns = [
    path('page/',views.loginPage,name = 'page'),
    path('action/', views.loginAction, name='action'),

]