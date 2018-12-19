#author_by zhuxiaoliang
#2018-12-10 下午6:17
from django import forms
from .models import UserProfile




class UserProfileForm(forms.Form):
    username = forms.CharField(max_length=32,required=True)
    password = forms.CharField(max_length=64,required=True)

class UploadImageForm(forms.ModelForm):


    class Meta:
        model = UserProfile

        fields = ['image']