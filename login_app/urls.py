#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 9:52
# @Author  : lilang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from login_app import views

urlpatterns = [
    path('page/',views.login_page,name = 'page'),
    path('logic/', views.login_logic, name='logic'),

]