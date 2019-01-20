from django.http import HttpResponse
from django.shortcuts import render,redirect
import json
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        # 接收post数据,并存储到数据库
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        uRepwd = request.POST['uRepwd']
        # 如果密码为空 或者 两次输入的密码不相等
        if uname == '' or upwd == '':
            resp = {'statuc':1,'message':'用户名和密码不能为空'}
            return HttpResponse(json.dumps(resp),content_type="application/json")
        elif upwd != uRepwd:
            resp = {'status':1,'message':'两次密码输入不一样'}
            return HttpResponse(json.dumps(resp),content_type="application/json")
            # return render(request,'register.html',resp)

        # return HttpResponse('接受到的用户名:%s,密码:%s'%(uname,upwd))
        # return HttpResponse('<script>console.log("hello world")</script>')