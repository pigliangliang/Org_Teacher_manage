

from datetime import datetime

import random

from django.db import models

# Create your models here.


class CourseOrg(models.Model):
    """
    机构信息

    """
    name = models.CharField('机构名',max_length=50)
    desc = models.TextField('机构描述')
    click_nums = models.IntegerField('点击数',default=0)
    fav_nums = models.IntegerField('收藏数',default=0)
    image = models.ImageField('封面图',upload_to='org/%Y%m',max_length=100)
    address = models.CharField('机构地址',max_length=100)
    city = models.ForeignKey('CityDict',verbose_name='所在城市',on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间',default=datetime.now)
    students = models.IntegerField("学习人数", default=random.randint(1,100))
    course_nums = models.IntegerField("课程数", default=random.randint(1,100))

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        return self.teacher_set.all().count()
    def get_course_nums(self):
        return self.course_set.all().count()

    def __str__(self):
        return  self.name


class CityDict(models.Model):
    """
    城市信息
    """
    name = models.CharField('城市', max_length=20)
    desc = models.CharField('描述', max_length=200)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Teacher(models.Model):
    """
    教师信息
    """
    org  = models.ForeignKey(CourseOrg,verbose_name='课程机构',on_delete=models.CASCADE)
    name = models.CharField('教师姓名',max_length=100)
    work_years = models.IntegerField('工作年限',default=1)
    work_company = models.CharField('就职公司', max_length=50)
    work_position = models.CharField('公司职位', max_length=50)
    points = models.CharField('教学特点', max_length=50)
    click_nums = models.IntegerField('点击数', default=0)
    fav_nums = models.IntegerField('收藏数', default=0)
    add_time = models.DateTimeField(default=datetime.now)
    image = models.ImageField(
        default='',
        upload_to="teacher/%Y/%m",
        verbose_name="头像",
        max_length=100)



    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name



    def __str__(self):
        return "[{0}]的教师: {1}".format(self.org, self.name)




