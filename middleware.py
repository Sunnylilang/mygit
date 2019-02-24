#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 14:32
# @Author  : lilang
# @Site    : 
# @File    : middleware.py
# @Software: PyCharm

import time

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import logging  # 引入logging模块
from redis import Redis
class Log:
    def __init__(self,logic):
        self.logic = logic
    def __call__(self, *args, **kwargs):
        ip = args[0].get_host()
        url = args[0].path
        logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        logging.info(ip + url)
        return self.logic(self,args[0])



class MyMiddleAware(MiddlewareMixin):

    @Log
    def process_request(self, request):
        redis = Redis(host='172.16.13.196', port=7007)
        ip = request.get_host()
        try:
            flag = int(redis.get(ip + 'flag'))
            if not flag:
                return HttpResponse("你走吧我妈不让我跟傻子玩")
            flag += 1
            if flag < 60:
                redis.set(ip + 'flag',flag)
            else:
                stop_time_stamp = time.time()
                start_time_stamp = int(redis.get(ip + 'start_time_stamp'))
                time_interval = stop_time_stamp - start_time_stamp
                if time_interval < 60:
                    redis.setex(ip + 'flag',10800,0)
        except:
            start_time_stamp = time.time()
            redis.mset({ip + 'flag':1,ip + 'start_time_stamp':start_time_stamp})



