from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'GET':
        #获取请求源地址,没有的话则获取一个'/',存session
        url = request.META.get('HTTP_REFERER','/')
        request.session['url'] = url

        # 先判断session中是否有登录信息
        if 'id' in request.session and 'uphone' in request.session:
            # 如果有则从哪来回哪去,否则继续判断cookie
            return redirect(url)
        else:
            # 否则继续判断cookie中是否有登录信息
            if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
                id = request.COOKIES['id']
                uphone = request.COOKIES['uphone']
                users = Users.objects.filter(id=id,uphone=uphone)
                if users:
                    # 如果正确,取出来判断,如果正确则保存进session,并从那来回哪去
                    request.session['id'] = id
                    request.session['uphone'] = uphone
                    return redirect(url)
                else:
                    # 如果不正确,先删除cookie中原有的值,再回到首页
                    # 构建响应对象并删除cookie的值再返回
                    form = ModelLoginForm()
                    resp = render(request,'login.html',{'form':form})
                    resp.delete_cookie('id')
                    resp.delete_cookie('uphone')
                    return resp
            else:
                # 如果有,则取出来判断
                # 如果没有,则取登录页面
                form = ModelLoginForm()
                return render(request,'login.html',locals())
    else:
        # 获取手机号码和密码,验证登录成功
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        user = Users.object.filter(uphone=uphone,upwd=upwd)

        # 成功:向下执行
        if user:
            # 将id和uphone存进session
            request.session['id'] = user[0].id
            request.session['uphone'] = uphone
            # 从session中获取原地址,并构建响应对象
            url = request.session['url']
            resp = redirect(url)
            # 判断是否要记住密码(保存进cookie)
            if 'savepwd' in request.POST:
                expire = 60*60*24*365
                resp.set_cookie('id',user[0].id,expire)
                resp.set_cookie('uphone',uphone,expire)
            # 从那来回那去
            return resp
        else:
            # 失败:回登录页
            form = ModelLoginForm()
            return render(request,'login.html',locals())

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        # post请求
        # 获取uphone的内容,并判断其是否存在
        uphone = request.POST.get('uphone')
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        users = Users.objects.filter(uphone=uphone)
        if users:
            # uphone已经存在,把提示信息拿到register页面上处理
            return render(request,'register.html',{'errMsg':'手机号码已存在'})
        else:
            users = Users()
            users.uphone = uphon
            users.upwd = upwd
            users.uname = uname
            users.uemail = request.POST['uemail']
            # 将users保存进数据库
            try:
                users.save()
                return redirect('/')
            except Exception as ex:
                print(ex)
                return render(request,'register.html',{'errMsg':'请联系管理员'})
            # 成功去往首页,失败给出提示



