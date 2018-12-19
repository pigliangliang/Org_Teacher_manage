#author_by zhuxiaoliang
#2018-12-16 下午9:07


from django.urls import path,re_path
from .views import  TeacherList,TeacherDetail

app_name = 'teacher'
urlpatterns =[

    path('teacherlist/<int:id>',TeacherList.as_view(),name='teacher_list'),
    path('teacherdetail/<int:id>',TeacherDetail.as_view(),name='teacher_detail')
]