from django.db import models

# Create your models here.

class Music(models.Model):
    # django中所有默认自带主键id,自增长属性
    # 属性 = models.字段类型(字段选项)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    website = models.URLField()