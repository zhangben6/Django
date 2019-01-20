from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

dic = {
    'name':'张奔',
    'age':22,
    'score':100
}

def index(request):
    return HttpResponse('这是fuxi应用中的首页')

def template_01(request):
    dic = {
        'name': '张奔',
        'age': 22,
        'score': 100
    }
    print(locals())
    return render(request,'01-template.html',locals())

# 示例静态文件的静态访问和动态访问
def static_views(request):
    return render(request,'02-static.html')

