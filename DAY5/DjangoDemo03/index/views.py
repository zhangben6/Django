from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Sum,Avg,Count,F,Q

#原生数据库操作方法
from django.db import connection


# Create your views here.

def add_author(request):
    # 方法1 使用Entry.objects.create()实现增加数据
    # author = Author.objects.create(name='莫言',age=65,email='moyan@163.com')
    # print(author)

    # 方法2 创建Entry的对象,并调用其save()
    # author = Author(name='鲁迅',age=95)
    # author.email = 'zhoushuren@163.com'
    # author.save()
    # print('ID:'+str(author.id))
    # print('NAME:'+author.name)
    # print('AGE:'+str(author.age))
    # print('Email:'+author.email)
    # print('isActive:'+str(author.isActive))

    # 方法3 创建字典并创建对象,并调用save()方法进行保存
    dic = {
        'name':'沈从文',
        'age':117,
        'email':'chencw@163.com',
        'isActive':False,
    }
    author = Author(**dic)
    author.save()
    print('ID:' + str(author.id))
    print('NAME:' + author.name)
    print('AGE:' + str(author.age))
    print('Email:' + author.email)
    print('isActive:' + str(author.isActive))

    return HttpResponse("<script>alert('增加数据成功')</script>")

def add_publisher(request):
    # publisher = Publisher.objects.create(name='人民文学出版社',address='北京三里屯',city='北京',country='China',website='www.RMWX.com')
    # print(publisher)

    # publisher = Publisher(name='上海译文出版社',address='上海闵行区航海大道',city='上海')
    # publisher.country = 'China'
    # publisher.website = 'www.yiwen.com'
    # publisher.save()

    dic = {
        'name':'长江文艺出版社',
        'address':'武汉市江阴区长江路57号',
        'city':'武汉',
        'country':'China',
        'website':'www.Cjwy.com',
    }
    publisher = Publisher(**dic)
    publisher.save()
    return HttpResponse("<script>alert('增加数据成功')</script>")

def add_book(request):
    # publisher = Publisher.objects.create(name='人民文学出版社',address='北京三里屯',city='北京',country='China',website='www.RMWX.com')
    book = Book.objects.create(title='金锁记',publicate_data='1988-02-15')
    return HttpResponse("<script>alert('增加数据成功')</script>")

def query(request):
    ############
    ###1.all()
    ############
    # authors = Author.objects.all()
    # print(authors.query)
    # 循环遍历authors中的每条数据
    # for au in authors:
    #     print('ID:%d,Name:%s,Age:%s'%(au.id,au.name,au.age))

    #############
    ##2.values()
    ############
    authors = Author.objects.values()
    # authors = Author.objects.values('id','email')
    print(authors)
    for au in authors:
        print('ID:%d,Name:%s'%(au['id'],au['name']))

    ##################
    ##3.values_list()
    ##################
    # authors = Author.objects.values_list('id','name','email')
    # print(authors)

    return HttpResponse("<script>alert('查询数据成功')</script>")

# 练习专用
def queryall(request):
    authors = Author.objects.all()
    # print(locals())
    return render(request,'03-queryall.html',locals())

def filter_views(request):
    ################
    ## filter()
    ################

    # 查询id为1的Author的信息
    # authors = Author.objects.filter(id=1).values('name')
    # print(authors)
    # print(authors.query)

    # 查询id为1并且name为莫言的Author的信息
    # authors = Author.objects.filter(id=1,name='莫言').all()
    # print(authors)
    # print(authors.query)

    # 练习
    # 1.查询Author表中age大于95的author信息
    # authors = Author.objects.filter(age__gt=95)
    # for au in authors:
    #     print(au.name)

    # 2.查询Author表中所有姓鲁的人的信息
    # authors = Author.objects.filter(name__startswith='鲁')
    # for au in authors:
    #     print(au.name)

    # 3.查询Author表中Email中包含'sh'的人的信息
    # authors = Author.objects.filter(email__contains='sh')
    # for au in authors:
    #     print(au.name)

    # 4.查询Author表中Age大于'鲁迅'的age的人的信息
    # authors = Author.objects.filter(age__gt=(Author.objects.filter(name='鲁迅').values('age'))).values('name','age')
    # print(authors)


    #####################
    ## 不等条件查询-exclude
    #####################

    # 1.查询id不等于1的所有的Author的信息
    # authors = Author.objects.exclude(id=1)
    # print(authors.query)
    # print(authors.values('name','age'))

    # 2.查询年龄不大于100的人的Author的信息
    authors = Author.objects.exclude(age__gt=100).values('name','age')  # exclude 相当于取反操作 | SQL: NOT
    print(authors.query)
    print(authors)


    return HttpResponse("Query OK!")


def update(request,id):
   #1.根据id查询出对应的Author的信息
    author=Author.objects.get(id=id)
    print(author)
    #2.将Author的信息渲染到05-update.html模板
    return render(request,'05-update.html',locals())


#################################################################################
# django第四天笔记   DAY04
#################################################################################
def aggregate(request):
    # 导入聚合函数  from django.db.models import Sum,Avg
    # 1.查询author表中所有人的年龄总和
    result = Author.objects.aggregate(sumAge=Sum('age'))
    print('年龄总和为:%d' % result['sumAge'])

    # 2.查询author表中所有人的平均年龄
    # result = Author.objects.aggregate(avgAge=Avg('age'))
    # print(result)

    # 3.查询Author表中年龄>=90的人的数量
    # result = Author.objects.filter(age__gt=90).aggregate(count=Count('age'))
    # print(result)


    return HttpResponse('Query Ok !!!')


########################
#### 带分组的查询 annotate
########################
def annotate(request):

    # 1.查询author表中isActive中为1和0的数量
    # 如果最后不追加values,则会显示{'isActive': True, 'count': 4}, {'isActive': False, 'count': 1}
    # result = Author.objects.values('isActive').annotate(count=Count('*'))
    # 追加后values('count')则对一个列进行显示,{'count': 4}, {'count': 1}
    # result = Author.objects.values('isActive').annotate(count=Count('*')).values('count')
    # print(result)



    # 2.查询每个时间所发布书籍的数量
    # result = Book.objects.values('publicate_data').annotate(count=Count('*'))
    # print(result)

    # 3.查询2000年之后所出版的图书数量
    # result = Book.objects.values('publicate_data').filter(publicate_data__gt='2000-01-01').annotate(count=Count('*'))
    # print(result)

    # 4.查询publisher中,City为北京的出版社数量
    # result = Publisher.objects.values('city').filter(city='北京').annotate(count=Count('*'))
    # result = Publisher.objects.filter(city='北京').aggregate(count=Count('*'))
    # print(result)

    #5.查询总共有几本图书
    # result = Book.objects.aggregate(count=Count('*'))
    # print(result)

    return HttpResponse("Query OK")

def update08(request):
    # 1.获取'巴金'
    # au = Author.objects.get(name='鲁迅')
    # 2.修改其email的值
    # au.email = 'zhendexiu@163.com'
    # 3.保存回数据库
    # au.save()

    # 修改所有人的isActive的值为True
    # Author.objects.all().update(isActive=True)

    #F查询 让所有人的年龄加10岁 F查询和Q查询的时候必须导入模块,类似于聚合函数的用法
    # Author.objects.all().update(age=F('age')+10)
    # Author.objects.all().update(age=F('age')+5)


    # Q查询 查询id=1或者isActive为True的人
    authors = Author.objects.filter(Q(id=1)|Q(isActive=True))
    print(authors)
    for au in authors:
        print('ID:%d,Name:%s,Age:%s'%(au.id,au.name,au.age))

    return HttpResponse('更新成功')

def delete09(request,id):
    # 根据id查询出对应的Author的信息
    au = Author.objects.get(id=id)
    au.isActive = False
    au.save()
    # 响应:重定向回/03-queryall
    return redirect('/03-queryall')


# 关系映射一对一的视图处理函数
def oto_views(request):
    # 创建一个 wife 对象并指定author信息再保存回数据库
    # 方式1:通过author_id属性关联
    # wife = Wife()
    # wife.name = '李夫人'
    # wife.age = 17
    # wife.author_set_id = 8
    # wife.save()

    # 方式2:通过author对象去关联
    # au = Author.objects.get(name='陈宏光')
    # wife = Wife()
    # wife.name = '陈夫人'
    # wife.age = 96
    #
    # # wife. 后面为Wife实体类的关联属性
    # wife.author_set = au
    # wife.save()
    #
    # return HttpResponse('增加夫人成功')



    # 正向查询 - 通过wife查询Author - 通过直接关联属性查询
    # wife = Wife.objects.get(id=1)
    # author = wife.author_set
    # print(type(author))  # 类型是 类
    #
    # print('作者姓名:%s,年龄:%d' % (author.name, author.age))
    # print('夫人姓名:%s,年龄:%d' % (wife.name, wife.age))

    # 反向查询 - 通过author查询wife - 通过隐士属性查询
    author = Author.objects.get(name='鲁迅')
    # 等号右边的wife为Author实体类中的隐式属性
    wife = author.wife
    print('作者姓名:%s,年龄:%d' % (author.name, author.age))
    print('夫人姓名:%s,年龄:%d' % (wife.name, wife.age))

    return HttpResponse('查询成功')

# 一对多的关系中  添加数据
def dtd_views(request):
    # book = Book(title='激荡十年',publicate_data='2010-01-09')
    book = Book.objects.get(id=5)
    book.publisher_id = 2
    book.save()
    return HttpResponse('添加成功')

def otm_views(request):
    # 一对多的正向查询 通过Book查询对应的Publisher
    # 查询id为3的书籍信息
    # book = Book.objects.get(id=3)
    # 查询对应的出版社
    # pub = book.publisher
    # print('出版社为:%s'%pub)


    # 一对多反向查询 - 通过publisher查询对应的所有的Book
    # 查询上海译文出版社的信息
    pub = Publisher.objects.get(name='郭童出版社')
    # 查询对应的所有的书籍 - book_set
    books = pub.book_set.all()

    return render(request,'11-otm.html',locals())

def mtm_views(request):
    # 增加数据:为Book绑定Author
    # 查询Book '蛙'
    # book = Book.objects.get(title='蛙')
    # 查询Author '张奔'
    # author = Author.objects.get(name='张奔奔')
    # 关联Book和Author
    # book.author_set.add(author)

    # 通过关联属性的remove()实现删除数据,删除book_author_set表中book和author的绑定关系 id值
    # book.author_set.remove(author)

    # return HttpResponse('OK')


    # 正向查询 - 通过Book查询Author
    # 查询book - 茶馆
    book = Book.objects.get(title='茶馆')
    # 获取对应的所有的Author
    authors = book.author_set.all()

    # 反向查询 - 查询Author查找Book
    # 查询Author - 鲁迅
    # au = Author.objects.get(name='鲁迅')

    # 获取对应所出版的书籍
    # books = au.book_set.all()

    return render(request,'12-mtm.html',locals())


def objects_views(request):
    count = Author.objects.age_count(90)
    return HttpResponse('年龄大于90的人数为%d' % count)


def exer_views(request):
    result = Author.objects.message('张').all()
    print(result)
    return HttpResponse('姓名查询成功')

def exer1_views(request):
    results = Book.objects.message('2010').all()
    print(results)
    for result in results:
        print('书名:%s,出版日期:%s'%(result.title,result.publicate_data))
    return HttpResponse('年份查询成功')
