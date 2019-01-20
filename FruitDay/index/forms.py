from django import forms
from .models import *

class ModelLoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uphone','upwd']
        labels={
            'uname':'手机号',
            'upwd':'密码',
        }
        widgets = {
            'uphone':forms.TextInput(attrs={'class':'uinput',}),
            'upwd':forms.PasswordInput(attrs={'class':'uinput','placeholder':'请输入6-20位字符'})
        }