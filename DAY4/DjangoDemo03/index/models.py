from django.db import models

# Create your models here.
# 创建一个实体类 - Publisher 表示"出版社"
# 1.name:出版社名称 - varchar
# 2.address:出版社地址 - varchar
# 3.city:出版社所在城市 - varchar
# 4.country:出版社所在国家 - varchar
# 5.website:出版社网址 - varchar
class Publisher(models.Model):
    # django中所有默认自带主键id,自增长属性
    # 属性 = models.字段类型(字段选项)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    website = models.URLField() # 长度默认为200

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name='邮箱')
    # 增加isActive表示是否处于启用状态 models.Boolean
    isActive = models.BooleanField(default=True,verbose_name='活动用户') # 必须添加默认值,否则不符合添加列的条件

    #通过 __str__ 修改django的后台页面index展现形式 localhost:8000/admin
    def __str__(self):
        return self.name

    #定义内部类-Meta
    class Meta:
        # 1.指定admin中显示的表名
        db_table = 'author'
        # 2.指定后台展现名称(单数)
        verbose_name = '作者'
        # 3.指定后台展现名称(复数)
        verbose_name_plural = verbose_name
        # 4.指定排序
        ordering = ['id']


class Book(models.Model):
    title = models.CharField(max_length=30)
    publicate_data = models.DateField()
    # 增加对Publisher(一)的引用关系
    publisher = models.ForeignKey(Publisher,null=True,verbose_name='出版社')

    # 增加对Author(多)的引用关系,不用加null=True,只是为了创建第三章表(book_author_set),不改变自己的表结构
    author_set = models.ManyToManyField(Author)




    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ['-publicate_data']




# wife -夫人
# name,age
class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')

    # 增加属性-author,表示与author表的一对一映射关系
    author_set = models.OneToOneField(Author,null=True,verbose_name='作者')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
        verbose_name = '夫人'
        verbose_name_plural = verbose_name
