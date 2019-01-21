from django import forms
from .models import *

#准备为level控件初始化数据
LEVEL_CHOICE = (
    ('1','好评'),
    ('2','中评'),
    ('3','差评'),
)


class RemarkForm(forms.Form):
    # 表示评论内容的表单控件们

    # 控件1 - 评论标题(subject) - 文本框
    # label : 控件前的标签文本
    subject = forms.CharField(label='标题')

    # 控件2 - Email(email) - Email框
    email = forms.EmailField(label='邮箱')

    # 控件3 - 评论内容(message) - Textarea
    # 注意: widget=forms.Textarea 为了将控件变为多行文本域
    message = forms.CharField(label='内容',widget=forms.Textarea)

    # 控件4 - 评论级别(level) - Select(下拉列表)
    level = forms.ChoiceField(
        label='级别',
        choices=LEVEL_CHOICE
    )

    # 控件5 - 是否保存(isSaved) - Checkbox
    isSaved = forms.BooleanField(
        label='是否保存',
    )


class RegisterForm(forms.Form):
    uname = forms.CharField(label='姓名')
    upwd = forms.CharField(label='密码')
    uage = forms.IntegerField(label='年龄')
    uemail = forms.EmailField(label='邮箱')
    isActive = forms.BooleanField(label='是否保存')


# forms模块的高级管理 将models于forms结合在一起
class ModelRegisterForm(forms.ModelForm):
    class Meta:
        # 1.指定关联的Model类  - model
        model = Users
        # 2.指定要生成控件的字段们 - fileds
        fields = '__all__'

        # 3.指定每个属性对应的label - labels
        labels = {
            'uname':'用户名称',
            'upwd':'用户密码',
            'uage':'用户年龄',
            'uemail':'电子邮件',
            'isActive':'是否保存'
        }


# 练习 使用两个字段创建对应的表单,进行登录验证操作,继承自forms.ModelForm
class ModelLoginForm(forms.ModelForm):
    class Meta:
        # 1.指定关联的Model类  - model
        model = Users
        # 2.指定要生成控件的字段们 - fileds
        fields = ['uname','upwd']

        # 3.指定每个属性对应的label - labels
        labels = {
            'uname':'登录名称',
            'upwd':'登录密码',
        }


class WidgetRegisterForm(forms.Form):
    # 用户名称 - type=text
    uname = forms.CharField(label='用户名称')
    # 用户密码 - type=password
    upwd = forms.CharField(label='用户密码',widget=forms.PasswordInput)
    # 评论级别 - type=radio
    level = forms.ChoiceField(label='评论级别',choices=LEVEL_CHOICE,widget=forms.RadioSelect)













