from django import forms

LEVEL_CHOICE={
    ('1','好评'),
    ('2','中评'),
    ('3','差评'),
}

class RemarkForm(forms.Form):
    subject = forms.CharField(label='标题')
    email = forms.EmailField(label='电子邮件')
    message = forms.CharField(label='内容',widget=forms.Textarea)
    level = forms.ChoiceField(label="级别",choices=LEVEL_CHOICE)
    isSaved = forms.BooleanField(label='是否保存')



# 创建高级管理类 继承自forms.ModelForm
class ModelLoginForm(forms.ModelForm):
    class Meta:
        model = Users
