#author_by zhuxiaoliang
#2018-12-09 下午2:18
from .views import index

from  django.urls import path,re_path

from .views import userlogout,userlogin,usereditpassword,userregister
app_name = 'user'

urlpatterns =[

    path('',index,name='index'),
    path('login/',userlogin,name='login'),
    path('register/',userregister,name='regiseter'),
    path('logout/',userlogout,name='logout'),
    path('editpassword/',usereditpassword,name='editpassword')

]