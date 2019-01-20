from django.contrib import admin
from .models import *

# 定义高级管理类
class AuthorAdmin(admin.ModelAdmin):
    # 1.定义在列表页上所显示的字段们
    list_display = ('name','age','email')
    # 2.定义在列表页上能够链接的字段们
    list_display_links = ('name','email')
    # 3.定义在列表页上能够被修改的字段们
    list_editable = ('age',)
    # 4.允许被搜索的字段们(实用功能)
    search_fields = ('name','email')
    # 5.右侧增加过滤器,实现快速的筛选
    list_filter = ('name','email')
    # 7.定义详情页中显示的字段以及顺序
    # fields = ('name','email','age','isActive')

    # 8.定义详情页中的字段分组
    fieldsets = (
        #分组1:组名:基本选项,字段:name,email
        ('基本选项',{
            'fields':('name','email')
        }),
        #分组2:组名:可选选项,字段:age,isActive 可折叠
        ('可选选项',{
            'fields':('age','isActive'),
            'classes':('collapse',)
        })
    )


class BookAdmin(admin.ModelAdmin):
    # 6.定义时间分层选择器
    date_hierarchy = 'publicate_data'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city')
    list_editable = ('address','city')
    list_filter = ('city',)
    search_fields = ('name','website')
    # 详情页中分组显示
    fieldsets = (
        ('基本信息',{
            'fields':('name','address','city'),

        }),
        (
            '高级信息',{
                'fields':('country','website'),
                'classes':('collapse',)
            }
        )
    )



# Register your models here.
# 注册需要管理的Models类.只有在此注册的models类才允许被管理
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife)