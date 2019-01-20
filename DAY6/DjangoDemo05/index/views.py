from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def test_views(request):
    return HttpResponse("<a href='/01-request'>测试的链接</a>")

def request_views(request): # request就是请求对象,它包含很多属性
    print(dir(request))
    print(request.method)
    print(request.body)
    print(request.scheme)
    print(request.COOKIES)
    print(request.META)
    print(request.path)
    # 判断有没有请求的源地址
    if 'HTTP_REFERER' in request.META:
        print('请求源地址:',request.META['HTTP_REFERER'])
    else:
        print('没有请求源地址')
    return HttpResponse('请求对象获取成功')


def post_views(request):
    # 判断请求方式,如果是get则去往02-post.html
    # 如果是post则接受请求提交数据
    if request.method == 'GET':
        return render(request,'02-post.html')
    else:
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        return HttpResponse('用户名称:%s,用户密码:%s'%(uname,upwd ))


def form_views(request):
    if request.method == 'GET':
        # 创建RemarkForm的对象,并发送到03-form.html上
        form = RemarkForm()
        return render(request,'03-form.html',locals())
    else:
        # 通过forms模块来获取提交的数据
        # 1.将提交的数据给RemarkForm()
        form = RemarkForm(request.POST)
        # 2.通过验证
        if form.is_valid():
            # 3.取值
            cd = form.cleaned_data
            print(cd)
            return HttpResponse('取值成功')
        return HttpResponse('取值失败')


def exer_views(request):
    if request.method == 'GET':
        # 使用自定义的From类
        form = RegisterForm()


        return render(request,'04-exer.html',locals())
    else:
        form = RegisterForm(request.POST)


        if form.is_valid():
            # 方法1  繁琐
            # cd = form.cleaned_data
            # print(cd['name'])
            # user = Users()
            # user.uname = cd['name']
            # user.upwd = cd['pwd']
            # user.uage = cd['age']
            # user.uemail = cd['email']
            # user.isActive = cd['isSaved']


            # 方法2 通过验证后,获取数据并构建成Users的对象
            user = Users(**form.cleaned_data)
            try:
                user.save()
                return HttpResponse('数据已成功存储到数据库')
            except Exception as ex:
                print(ex)
                return HttpResponse('数据库存储不成功')
        return HttpResponse('取值失败')


def login_views(request):
    if request.method == 'GET':
        # 使用关联Model的Form类
        form = ModelLoginForm()

        return render(request,'05-login.html',locals())
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        #验证登录
        users = Users.objects.filter(uname=uname,upwd=upwd)
        if users:
            return HttpResponse('登录成功')
        return HttpResponse('登录失败')


def widget01(request):
    form = WidgetRegisterForm()
    return render('request','06-widget.html',locals())



#########################DAY7####################
def set_cookie(request):
    resp = HttpResponse("成功响应数据到客户端")
    expired = 60*60*24*365
    resp.set_cookie('USERID','37778234',expired)
    return resp

# 响应对象存储cookie,请求对象取出cookie


def get_cookie(request):
    print(request.COOKIES)
    if 'USERID' in request.COOKIES:
        print('userid的值为:'+request.COOKIES['USERID'])

    return HttpResponse('获取cookie成功')


def set_session(request):
    request.session['USERID'] = '348343'
    request.session['UNAME'] = 'lixiaochao'
    return HttpResponse('session数据保存成功')


def get_session(request):
    uid = request.session['USERID']
    uname = request.session['UNAME']
    return HttpResponse('UID:%s,UNAME:%s'%(uid,uname))