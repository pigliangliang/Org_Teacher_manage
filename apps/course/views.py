from django.shortcuts import render

# Create your views here.

from django.views.generic import View,DetailView,ListView

from .models import Course,Lesson,CouresResourse
from django.http import HttpResponse

from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage,Page
from operation.models import CoureseComment
from operation.models import UserCourse,UserProfile





class CourseList(ListView):
    template_name = 'course-list.html'
    context_object_name = 'course'
    model = Course

    # def get_queryset(self):
    #     if self.request.GET.get('sort')=='':
    #         return Course.objects.all()
    #     elif self.request.GET.get('sort')=='hot':
    #         return Course.objects.order_by('-click_nums')
    #     else:
    #         return Course.objects.order_by('-students')

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.GET.get('sort') == '':
            kwargs['course']=Course.objects.all()
            kwargs['sort']=''
        elif self.request.GET.get('sort')=='hot':
            kwargs['course']=Course.objects.order_by('-click_nums')
            kwargs['sort']='hot'
        else:
            kwargs['course']= Course.objects.order_by('-students')
            kwargs['sort']='students'

        paginator = Paginator(kwargs['course'], 3)

        page = self.args[0]

        try:
            pageInfo = paginator.page(page)
        except PageNotAnInteger:
            pageInfo = paginator.page(1)
        except EmptyPage:  # 超过最大页数，返回最大页的内容
            pageInfo = paginator.page(paginator.num_pages)
        kwargs['course'] = pageInfo
        kwargs['hot_course']=Course.objects.order_by('-click_nums')[:2]
        return super(CourseList,self).get_context_data(**kwargs)


class CourseDetail(DetailView):
    context_object_name = 'course'
    template_name = 'coursedetail.html'
    model = Course
    pk_url_kwarg = 'id'

"""


class CourseInfo(DetailView):
    context_object_name = 'course'
    model = Course
    template_name = 'coursevideo.html'

    pk_url_kwarg = 'id'


    def get_context_data(self, **kwargs):
        #先筛选该课程的所有章节
        kwargs['lesson'] = self.object.lesson_set.all()
        #根据章节id进行筛选所有的视屏
        kwargs['video'] =[]
        for lesson in self.object.lesson_set.all():

            kwargs['video'].append(Lesson.objects.get(id=lesson.id).video_set.all())


        return super(CourseInfo,self).get_context_data(**kwargs)
"""

class CourseInfo(View):
    def get(self,request,id):


        d = {}
        course = Course.objects.get(id=id)

        learn_course = UserCourse.objects.filter(user=request.user,course_id=id)

        if not learn_course:
            u = UserCourse.objects.create(user=request.user,course=course)
            u.save()


        print(course.get_course_lesson)
        #获取课程所有的章节
        #d['lesson'] = course.lesson_set.all()
        # 遍历章节id获取所有的视屏
        for lesson in course.lesson_set.all():
            if lesson.id not in d.keys():
                    d[lesson.name]= [Lesson.objects.get(id=lesson.id).video_set.all()]
            else:
                d[lesson.name].append(Lesson.objects.get(id=lesson.id).video_set.all())
        course_resourse = CouresResourse.objects.filter(course=course)#正向查询


        #课程的评论
        comments = course.couresecomment_set.all()

        #获取该课程的用户，通过后去用户学习的其他课程
        user_courses = UserCourse.objects.filter(course=course)
        #通过用户获取用户的课程
        user_ids = [user_course.user_id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        course_ids = [all_user_course.course_id for all_user_course in all_user_courses]
        courses = Course.objects.filter(id__in=course_ids).order_by('-click_nums').exclude(id=id)[:3]


        return render(request,'coursevideo.html',locals())



    def post(self,request,id):
        if request.user.is_authenticated:
            course = Course.objects.get(id=id)
            comment = self.request.POST.get('comment')
            course.couresecomment_set.create(user=request.user,comment=comment)

        #get 页面
        d = {}
        course = Course.objects.get(id=id)
        for lesson in course.lesson_set.all():
            if lesson.id not in d.keys():
                    d[lesson.name]= [Lesson.objects.get(id=lesson.id).video_set.all()]
            else:
                d[lesson.name].append(Lesson.objects.get(id=lesson.id).video_set.all())
        course_resourse = CouresResourse.objects.filter(course=course)#正向查询



        comments = course.couresecomment_set.all()
        return render(request,'coursevideo.html',locals())

class AddComment(View):
    def post(self,request):
        comments = self.request.POST.get('comments')
        couser_id = self.request.POST.get('course_id')

        Course.objects.get(id=couser_id).couresecomment_set.create(user=request.user,comment=comments)
        return HttpResponse('{"status":"success"}',content_type='application/json')


