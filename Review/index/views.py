from django.db.models import Sum, Avg, Count, F, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return HttpResponse('这是INDEX应用中的首页')

def login(request):
    return HttpResponse('这是INDEX应用中的登录页')

def register(request):
    return HttpResponse('这是INDEX应用中的注册页')

def add_author(request):
    author = Author.objects.create(name='巴金',age=80,email='Bajin@163.com')
    author.save()
    return HttpResponse('添加作者信息成功')

def add_punlisher(request):
    publisher = Publisher.objects.create(name='中国人民出版社',address='通州区丹尼斯大楼1507',city='北京',country='China',website='www.ChinaPeople.com')
    publisher.save()
    return HttpResponse('添加出版社成功')

def add_book(request):
    book = Book.objects.create(title='茶馆',publicate_data='2015-06-06')
    book.save()
    return HttpResponse('添加图书信息成功')

def query(request):
    # authors = Author.objects.all()
    # print(authors.query)
    # print(authors)
    # for au in authors:
    #     print(au.id,au.name,au.age)

    # values() 结尾
    # authors = Author.objects.values()
    # print(authors)
    # for au in authors:
    #     print(au['id'],au['name'])

    # values_list() 查询指定字段
    authors = Author.objects.values_list('id','name')
    print(authors)
    for au in authors:
        print(au[0],au[1])

    return HttpResponse('查询成功')

# 让author 显示在网页上
def queryall(request):
    authors = Author.objects.all()
    return render(request,'03-queryall.html',locals())

def filter_views(request):
    # filter() 的用法
    # 查询id=1的信息
    # authors = Author.objects.filter(id=1).values('name')
    # print(authors)

    # authors = Author.objects.filter(id=1,name='沈从文').values('name')
    # print(authors)

    # author = Author.objects.filter(age__gt=30).values('name')
    # print(author)

    # author = Author.objects.filter(name__startswith='老').values('name')
    # print(author)

    # 不等条件查询
    # authors = Author.objects.exclude(id=1).values('name')
    # print(authors)

    # authors = Author.objects.exclude(age__gte=100).values('name','age')
    # print(authors)

    # 排序查询
    # authors = Author.objects.order_by('-name').values('name')
    # print(authors)

    #只查询一条数据
    # author = Author.objects.get(id=1)
    # print(type(author))  # 类型是 类

    # 聚合查询

    return HttpResponse('查询成功')

# 网页作者信息修改页面
def update(request,id):
    # 根据id查询出对应的Author信息
    author = Author.objects.get(id=id)
    print(author)

    return render(request,'05-update.html',locals())

def aggregate(request):
    # result = Author.objects.aggregate(sumAge=Sum('age'))
    # print(result)

    # 返回值的形式是字典
    # result = Author.objects.aggregate(sumAge=Avg('age'))
    # print(result)

    result = Author.objects.filter(age__gt=60).aggregate(avgage=Avg('age'))
    print(result)
    return HttpResponse('查询成功')

def annotate(request):
    # result = Book.objects.values('publicate_data').annotate(count=Count('*'))
    # print(result)

    # 4.查询publisher中,City为北京的出版社数量
    result = Publisher.objects.values('city').filter(city='北京').annotate(count=Count('*'))
    print(result)
    return HttpResponse('查询成功')

def update08(request):
    # au = Author.objects.get(name='巴金')
    # au.email = 'Baniubi@163.com'
    # au.save()

    # 批量修改:  修改所有人的isActive的值为1
    Author.objects.all().update(isActive=True)

    # Author.objects.all().update(age=F('age')+10)

    # Q查询 查询id=1或isActive为True的人
    authors = Author.objects.filter(Q(id=1)|Q(isActive=True))
    print(authors)

    return HttpResponse('更新成功')

def delete(request,id):
    author = Author.objects.get(id=id)
    author.isActive = False
    author.save()
    return redirect('/03-queryall')


def oto_views(request):
    # 方式1
    # 通过author_set_id去关联添加对应
    # wife = Wife()
    # wife.name = '沈夫人'
    # wife.age = 75
    # wife.author_set_id = 1
    # wife.save()

    # 方式2
    # 通过author_set属性去关联
    # au = Author.objects.get(name='老舍')
    # wife = Wife()
    # wife.name = '老夫人'
    # wife.age = 80
    # wife.author_set = au
    # wife.save()

    # return HttpResponse('增加夫人成功')

    # 正向查询数据 - 通过wife查询对应的Author - 通过直接关联属性author_set
    # wife = Wife.objects.get(id=1)
    # author = wife.author_set
    # print('作者姓名:%s,作者年龄:%s'%(author.name,author.age))
    # print('夫人姓名:%s,夫人年龄:%s'%(wife.name,wife.age))
    #
    # 反向查询对应的数据 - 通过Author 查询 对应的Wife - 通过隐式属性wife查询
    author = Author.objects.get(name='老舍')
    wife = author.wife
    print('作者姓名:%s,作者年龄:%s' % (author.name, author.age))
    print('夫人姓名:%s,夫人年龄:%s' % (wife.name, wife.age))
    return HttpResponse('查询成功')

def otm_views(request):
    # 对book增加关联数据(方法1) - 通过publisher_id
    # book = Book.objects.get(id=1)
    # book.publisher_id = 1
    # book.save()
    # 增加关联数据 (方法2) - 通过publisher关联属性
    # pub = Publisher.objects.get(id=2)
    # book = Book.objects.get(id=2)
    # book.publisher = pub
    # book.save()
    # 增加全新的数据并关联Publisher
    # book = Book(title='激荡十年',publicate_data='2015-12-26')
    # book.publisher_id = 2
    # book.save()

    # return HttpResponse('添加关联数据成功')

    # 多对多的正向查询数据
    # book = Book.objects.get(id=1)
    # pub = book.publisher_id
    # print(type(pub))
    # print('书名:%s'% book.title)
    # print('出版社名称:%s'% pub)

    # 反向查询
    pub = Publisher.objects.get(id=2)
    book = pub.book_set.all()
    print(book)

    return HttpResponse('查询成功')

def mtm_views(request):
    # 增加数据
    # book = Book.objects.get(title='丰乳肥臀')
    # author = Author.objects.get(id=3)
    # book.author_set.add(author)
    # return HttpResponse('OJBK')

    # 正向查询数据 通过关联属性 author_set
    # book = Book.objects.get(id=1)
    # authors = book.author_set.all()
    # return render(request,'12-mtm.html',locals())

    # 反向查询数据 通过隐式属性book_set
    author = Author.objects.get(id=1)
    books = author.book_set.all()
    return render(request,'12-mtm.html',locals())


def object_views(request):
    count = Author.objects.age_count(90)
    return HttpResponse('年龄大于90的人数为%d'%count)

def post_views(request):
    if request.method == 'GET':
        return render(request,'13-post.html')
    else:
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        return HttpResponse('用户名称:%s,密码:%s'%(uname,upwd))

def form_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request,'14-form.html',locals())
    else:
        form = RemarkForm(request.POST)
        if form.is_valid():
            res = form.cleaned_data
            print(res)
            return HttpResponse('取值成功')
        return HttpResponse('取值失败')

