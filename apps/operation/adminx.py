#author_by zhuxiaoliang
#2018-12-10 下午3:13


# operation/adminx.py

import xadmin

from .models import UserAsk, UserCourse, UserMessage, CoureseComment, UserFavrite


class UserAskAdmin(object):
    '''用户表单我要学习'''

    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


#
class UserCourseAdmin(object):
    '''用户课程学习'''

    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']



class UserMessageAdmin(object):
    '''用户消息后台'''

    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']



class CourseCommentsAdmin(object):
    '''用户评论后台'''

    list_display = ['user', 'coures', 'comment', 'add_time']
    search_fields = ['user', 'coures', 'comment']
    list_filter = ['user', 'coures', 'comment', 'add_time']



class UserFavoriteAdmin(object):
    '''用户收藏后台'''

    list_display = ['user', 'av_id', 'fav_type', 'add_time']
    search_fields = ['user', 'av_id', 'fav_type']
    list_filter = ['user', 'av_id', 'fav_type', 'add_time']


# 将后台管理器与models进行关联注册。
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CoureseComment, CourseCommentsAdmin)
xadmin.site.register(UserFavrite, UserFavoriteAdmin)