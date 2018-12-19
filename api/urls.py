#author_by zhuxiaoliang
#2018-12-06 上午12:00

from django.urls import path,re_path
from .views import AuthView,OrderView,VipOrderView
urlpatterns =[

    path('api_auth/',AuthView.as_view()),
    path('order/',OrderView.as_view()),
    path('viporder/',VipOrderView.as_view())
]