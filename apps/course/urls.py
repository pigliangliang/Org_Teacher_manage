#author_by zhuxiaoliang
#2018-12-13 下午9:

from django.urls import path,re_path
from  .views import CourseList,CourseDetail,CourseInfo

from .views import AddComment




app_name = 'course'
urlpatterns =[

    #path('courselist/',CourseList.as_view(),name='course_list'),
    re_path('courselist/(\d+)',CourseList.as_view(),name='course_list'),
    path('coursedetail/<int:id>/',CourseDetail.as_view(),name='coursed_etail'),
    path('courseinfo/<int:id>/',CourseInfo.as_view(),name='courseinfo'),
    path('addcomment/',AddComment.as_view(),name='add_comment'),




]