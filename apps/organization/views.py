from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

from .models import CourseOrg,CityDict
from django.views import View

from django.views.generic import ListView,DetailView
from .forms import UserForm
from django.http  import HttpResponse
from course.models import  Course,Teacher
from operation.models import UserFavrite

class OrgView(ListView):

    def get(self, request, *args, **kwargs):
        all_orgs = CourseOrg.objects.all()
        org_onums = all_orgs.count()
        # 取出所有城市
        all_citys = CityDict.objects.all()

        city_id = request.GET.get('city', '')#城市
        ct_id = request.GET.get('ct','')#机构
        sort = request.GET.get('sort','')
        if city_id  :
            all_orgs = all_orgs.filter(city_id=int(city_id))
        if ct_id:
            all_orgs = all_orgs.filter(id=int(ct_id))
        if sort=='students':
            all_orgs = all_orgs.order_by('-students')
        else:
            all_orgs = all_orgs.order_by('-course_nums')
        paginator = Paginator(all_orgs,2)

        page = args[0]

        try:
            pageInfo = paginator.page(page)
        except PageNotAnInteger:
            pageInfo = paginator.page(1)
        except EmptyPage:#超过最大页数，返回最大页的内容
            pageInfo = paginator.page(paginator.num_pages)

        #点击率排名
        hot_orgs = CourseOrg.objects.all().order_by('-click_nums')[:3]




        return render(request, "org-list.html",locals())


class UserAskView(View):

    # def get(self,request):
    #     uf = UserForm()
    #     return  render(request,'org-list.html',{'uf':uf})

    def post(self,request):
        uf = UserForm(request.POST)
        if uf.is_valid():
            uf.save()
            return  HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')





class OrgHomeView(ListView):

    template_name = 'org-detail-homepage.html'
    context_object_name = 'courseorg'

    def get_queryset(self):
        return CourseOrg.objects.get(id=self.args[0])
    def get_context_data(self, **kwargs):
        kwargs['course'] = CourseOrg.objects.get(id=self.args[0]).course_set.all()[:4]#反向查询
        kwargs['teacher'] = Course.objects.filter(course_org=self.args[0])[:4]#正向查询
        return super(OrgHomeView,self).get_context_data(**kwargs)



class OrgHomeDetail(DetailView):
    template_name = 'org-detail-homepage.html'
    context_object_name = 'courseorg'
    pk_url_kwarg = 'id'
    model = CourseOrg
    current_page ='home'

    # def get_object(self, queryset=None):
    #     return super(OrgHomeDetail,self).get_object()

    def get_context_data(self, **kwargs):
        kwargs['course'] = self.object.course_set.all()[:4]#反向查询
        kwargs['teacher'] = self.object.teacher_set.all()
        kwargs['current_page'] = self.current_page
        return super(OrgHomeDetail,self).get_context_data(**kwargs)

class OrgCourseView(ListView):
    model =  CourseOrg
    template_name = 'orgcourse.html'
    context_object_name = 'course'
    current_page= 'course'

    def get_queryset(self):
        return CourseOrg.objects.get(id=self.args[0]).course_set.all()#课程queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['courseorg']=CourseOrg.objects.get(id=self.args[0])
        kwargs['current_page']=self.current_page
        return super(OrgCourseView,self).get_context_data(**kwargs)


class OrgDetailView(DetailView):
    template_name = 'orgdetail.html'
    model = CourseOrg
    context_object_name = 'courseorg'
    current_page='desc'
    pk_url_kwarg = 'pk'

    """
    使用detailView无需重写该方法，Detailview已经根据pk_url_kwarg
    中获取的参数实现获取具体pk的queryset。
    """
    # def get_object(self, queryset=None):
    #     return CourseOrg.objects.get()

    def get_context_data(self, **kwargs):
        kwargs['current_page']=self.current_page
        return super(OrgDetailView,self).get_context_data(**kwargs)

class OrgTeacherView(DetailView):
    template_name = 'orgteacher.html'
    model = CourseOrg
    context_object_name = 'courseorg'
    current_page= 'teacher'

    pk_url_kwarg = 'id'

    #self.object 已经是通过id过滤的机构
    def get_context_data(self, **kwargs):
        kwargs['teacher'] = self.object.teacher_set.all()
        kwargs['current_page'] =self.current_page
        return super(OrgTeacherView,self).get_context_data(**kwargs)


class UserFavView(View):
    def post(self,request):
        av_id = request.POST.get('fav_id')
        fav_type = request.POST.get('fav_type')

        if request.user.is_authenticated:
            print(request.user.username)
            record = UserFavrite.objects.filter(user=request.user,av_id=av_id,fav_type=fav_type)
            if record:
                record.delete()
                return HttpResponse('{"status":"success", "msg":"收藏"}',content_type='application/json')
            else:
                UserFavrite.objects.create(user=request.user,av_id=av_id,fav_type=fav_type)
                return HttpResponse('{"status":"success", "msg":"已收藏"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}',content_type='application/json')


class TeacherList(ListView):
    template_name = 'teacher-list.html'
    context_object_name = 'teacher'
    queryset = Teacher.objects.all()

    paginate_by = 4

    # def paginate_queryset(self, queryset, page_size):
    #     return super(TeacherList,self).paginate_queryset(queryset=queryset,page_size=3)
    #




    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['count']= Teacher.objects.all().count()
        return super(TeacherList,self).get_context_data(**kwargs)



class TeacherDetail(DetailView):
    template_name = 'teacherdetail.html'
    model = Teacher
    context_object_name = 'teacher'
    pk_url_kwarg = 'id'


    def get_context_data(self, **kwargs):
        kwargs['teacher_sort'] = Teacher.objects.order_by('-click_nums')[:2]
        kwargs['course'] =self.object.course_set.all()
        kwargs['org']=CourseOrg.objects.get(id=self.object.org_id)
        print(kwargs.items())

        has_teacher_faved = False

        teacher  = self.object
        print(self.object)

        if UserFavrite.objects.filter(user=self.request.user,fav_type=3,av_id=teacher.id):
            has_teacher_faved = True

        print(teacher.id)

        has_org_faved = False

        if UserFavrite.objects.filter(user=self.request.user,fav_type=2,av_id=self.object.org_id):
            has_org_faved = True

        kwargs['has_teacher_faved'] = has_teacher_faved

        kwargs['has_org_faved'] = has_org_faved


        return  super(TeacherDetail,self).get_context_data(**kwargs)





