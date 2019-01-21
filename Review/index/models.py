from django.db import models

# Create your models here.


# 创建自定义模型类,继承自models.Manager
class AuthorManager(models.Manager):
    # 自定义方法
    def age_count(self,age):
        return self.filter(age__gte=age).count()
    def message(self,str):
        return self.filter(name__contains=str)


class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='名称')
    address = models.CharField(max_length=200,verbose_name='地址')
    city = models.CharField(max_length=20,verbose_name='城市')
    country = models.CharField(max_length=20,verbose_name='国家')
    website = models.URLField(verbose_name='网址') # 长度默认为20
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name
        ordering = ['id']

class Author(models.Model):
    objects = AuthorManager()
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name='电子邮箱')
    isActive = models.BooleanField(default=True,verbose_name='活动用户')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name
        # 按id的升序排列
        ordering = ['id']

class Book(models.Model):
    title = models.CharField(max_length=30,verbose_name='书名')
    publicate_data = models.DateField(verbose_name='出版时间')
    # 增加对publisher(一)的引用关系字段
    publisher = models.ForeignKey(Publisher,null=True,verbose_name='对应出版社')

    # 增加对Author(多)的引用关系,为了创建第三张表,不用加null=True
    author_set = models.ManyToManyField(Author)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ['id']

# 增加wife(夫人)实体类,一对一关系映射 Author : Wife
class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')

    # 增加属性 author_set 表示与Author的一对一关系
    author_set = models.OneToOneField(Author,null=True,verbose_name='作者')
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
        verbose_name = '夫人'
        verbose_name_plural = verbose_name
        ordering = ['id']



