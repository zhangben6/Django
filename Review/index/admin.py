from django.contrib import admin
from .models import *
# Register your models here.

# 编写高级admin类
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','age','email']
    list_display_links = ['name','email']
    list_editable = ['age']
    search_fields = ['name','email']
    list_filter = ('name',)
    # 定义作者详情页的分组显示
    fieldsets = (
        ('基本选项',{
            'fields':('name','email')
        }),
        (
            '可选选项',{
                'fields':('age','isActive'),
                # 设置折叠效果
                'classes': ('collapse',)

            }
        )
    )


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name','address','city']
    list_editable = ['address','city']
    list_filter = ('city',)
    search_fields = ['city','name','address','website']
    fieldsets = (
        ('基本信息',{
            'fields':('name','address','city')
        }),
        (
            '高级信息',{
                'fields':('country','website'),
                'classes':('collapse',)
            }
        )
    )



# 注册需要管理的Models实体类
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book)
admin.site.register(Wife)