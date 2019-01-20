from audioop import reverse

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.

dic={
    'name':'张奔',
    'age':21,
    'specialty':'basketball'
}

def index(request):
    return HttpResponse("这是music应用中的index访问路径")

def template_views(request):
    # 方法1
    t = loader.get_template('01-template.html')
    html = t.render(dic)
    return HttpResponse(html)

    # 方法2
    # return render(request,'01-template.html',dic)

def var_views(request):
    uname = "wangwc"
    uage = 37
    list = ['王老师','王夫人','李小超']
    dic = {
        'SWK':'孙悟空',
        "ZWN":'猪无能',
        'WWC':'王伟超',
    }
    person = Person()
    person.uname = '哲学吕'
    print(locals())
    return render(request,'02-var.html',locals())

class Person(object):
    uname = None
    def intro(self):
        return 'hello my name is %s' % self.uname

def lianxi(request):
    list = ['孙悟空', '西门庆', '曹操', '林黛玉']
    return render(request,'lianxi.html',locals())

def static_views(request):
    return render(request,'03-static.html')

def parent(request):
    return render(request,'04-parent.html')

def child(request):
    return render(request,'05-child.html')

def test_views(request):
    return HttpResponse('<h1>This is test views</h1>')

def reg_views(request,num):
    return HttpResponse('<h1>传递过来的值为:%s</h1>' % num)

