from datetime import datetime


from django.db import models
# Create your models here.
from users.models import UserProfile
from course.models import Course
class UserAsk(models.Model):
    """
    用户咨询表
    """
    name = models.CharField('姓名', max_length=20)
    mobile = models.CharField('手机', max_length=11)
    course_name = models.CharField('课程名', max_length=50)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name






class UserMessage(models.Model):
    """
    用户消息表
    """


    user = models.IntegerField('接受用户', default=0)
    message = models.CharField('消息内容', max_length=500)
    has_read = models.BooleanField('是否已读', default=False)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name



class CoureseComment(models.Model):
    """
    用户评论表
    """
    user = models.ForeignKey(UserProfile,verbose_name="用户",on_delete=models.CASCADE)
    comment = models.TextField('评论内容')
    coures = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField('评论时间',default=datetime.now)


    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural =verbose_name



class UserCourse(models.Model):
    """
    用户学习课程表
    """
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间',default=datetime.now)


    class Meta:
        verbose_name = '用户课程表'
        verbose_name_plural = verbose_name



class UserFavrite(models.Model):
    """
    用户收藏表
    """
    FAV_TYPE = (
        (1, '课程'),
        (2, '课程机构'),
        (3, '讲师')
    )

    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    av_id = models.IntegerField('数据id', default=0)
    fav_type = models.IntegerField(verbose_name='收藏类型', choices=FAV_TYPE, default=1)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name




