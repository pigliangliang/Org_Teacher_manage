#author_by zhuxiaoliang
#2018-12-11 下午4:52


from django import forms
from operation.models import UserAsk

class UserForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = [
            'name','mobile','course_name',
        ]
