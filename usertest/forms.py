#author_by zhuxiaoliang
#2018-12-09 下午2:26


from django.contrib.auth.models import User

from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']