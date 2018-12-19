"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
import xadmin
from django.views.generic import TemplateView
from users.views import LoginView,IndexView,userlogout,RegisterView,ForgetView,ActiveUserView
from users.views import RestView
from django.views.static import serve
from untitled1.settings import MEDIA_ROOT
from  organization.views import OrgView,UserAskView,OrgHomeView,OrgHomeDetail,OrgCourseView


from organization.views import OrgDetailView,OrgTeacherView
from organization.views import UserFavView



urlpatterns = [

    path('api-auth/', include('rest_framework.urls',)),
    path('admin/', xadmin.site.urls),
    #path('user/',include('api.urls')),
    #path('user/',include('app01.urls'))，
    path('user/',include('usertest.urls',namespace='user')),
    path('',IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',userlogout,name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('forget/',ForgetView.as_view(),name='forget'),
    re_path('active/(\w+)/',ActiveUserView.as_view()),
    re_path('reset/(\w+)/',RestView.as_view()),
    #path('org_list/$',OrgView.as_view(),name='org_list'),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    re_path(r'org_list/(\d+)/$',OrgView.as_view(),name='org_list'),
    path('userask/',UserAskView.as_view(),name='userask'),
    #path('forumlink/',include('forumlink.urls',namespace='forumlink')),
    #两种方式的url，对应到view中的参数是不一样的。正则方式在view中需要通过参数的方式
    #获取，有两种方式
    #一：函数形式参数传递：
    #def get（request,id）
    #二：通过arg获取 arg【0】
    #url中定义了参数id，view中必须对应到，具体参考代码示例。
    #re_path('orghome/(\d+)/',OrgHomeView.as_view(),name='orghome'),
    path('orghome/<str:id>/', OrgHomeDetail.as_view(), name='orghome'),

    re_path('orgcourse/(\d+)/',OrgCourseView.as_view(),name='orgcourse'),
    path('orgdetail/<int:pk>/',OrgDetailView.as_view(),name='orgdetail'),
    path('orgteacher/<int:id>/',OrgTeacherView.as_view(),name='orgteacher'),
    path('userfav/',UserFavView.as_view(),name='userfav'),
    path('course/',include('course.urls',namespace='course')),
    path('teacher/',include('organization.urls',namespace='teacher')),
    path('users/',include('users.urls',namespace='users')),
]
