#author_by zhuxiaoliang
#2018-12-17 下午7:30


from django.urls import path,re_path

from .views import UserInfo

app_name ='users'

urlpatterns = [

    path('userinfo/<int:id>',UserInfo.as_view(),name='userinfo')
]