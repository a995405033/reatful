from django.shortcuts import HttpResponse
import json

def index(request):
    dict = {"test":"test"}
    return HttpResponse(json.dumps(dict))

from django.shortcuts import render

# Create your views here.

import time
from sqLite3 import models
from django.http import JsonResponse
from rest_framework.views import APIView

class AuthView(APIView):


    def post(self,request,*args,**kwargs):
        ret = {'code':1000,'msg':None}
        try:
            # 参数是datadict 形式
            usr = request._request.POST.get('username')
            pas = request._request.POST.get('password')

            print(usr)
            obj = models.User.objects.filter(username=usr,password=pas).first()
            if not obj:
                ret['code'] = '1001'
                ret['msg'] = '用户名或者密码错误'
                return JsonResponse(ret)
                # 里为了简单，应该是进行加密，再加上其他参数
            token = str(time.time()) + usr
            print("token",token)
            models.userToken.objects.update_or_create(username=obj, defaults={'token': token})
            ret['msg'] = '登录成功'
            #ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)