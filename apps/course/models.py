from datetime import datetime


from django.db import models

# Create your models here.
from organization.models import CourseOrg,Teacher

class Course(models.Model):

    DEGREE_CHOICE=(
        ("cj", "初级"),
        ("zj", "中级"),
        ("gj", "高级")
    )



    name = models.CharField("课程名",max_length=32,null=False)
    desc = models.CharField('课程描述',max_length=300)
    detail = models.TextField('课程详情')
    degree = models.CharField('难度',choices=DEGREE_CHOICE,max_length=2)
    learn_time = models.IntegerField('学习时长',default=0)
    students = models.IntegerField('学习人数',default=0)
    fav_nums = models.IntegerField('收藏人数',default=0)
    image = models.ImageField('封面图',upload_to='course/%Y/%m',max_length=100,blank=True)
    click_nums = models.IntegerField('点击数',default=0)
    add_time = models.DateTimeField('添加时间',default=datetime.now)
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构", null=True, blank=True)
    teacher = models.ForeignKey(Teacher,verbose_name='教师',on_delete=models.CASCADE,null=True,blank=True)
    youneed_know = models.CharField('课程须知', max_length=300, default='')
    teacher_tell = models.CharField('老师告诉你', max_length=300, default='')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


    def get_course_lesson(self):
        self.lesson_set.all()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    name = models.CharField('章节名',max_length=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)


    class Meta:
        verbose_name = '章节名'
        verbose_name_plural = verbose_name


    def get_lesson_video(self):
        return self.video_set.all()


    def __str__(self):
        return "{}课程的{}节".format(self.course,self.name)


class  Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name='章节',on_delete=models.CASCADE)
    name =models.CharField('视频名',max_length=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)


    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CouresResourse(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField('资源名',max_length=100)
    download = models.FileField('资源文件',upload_to="course/resource/%Y/%m",max_length=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)


    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name


    def __str__(self):
        return "{}课程的资源{}".format(self.course.name,self.name)





