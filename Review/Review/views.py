from django.http import HttpResponse


def demo1(request,year):
    return HttpResponse('带参数的url,后四位输入的数字为:%s'%year)