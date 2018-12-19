#author_by zhuxiaoliang
#2018-12-19 下午2:25


from django.utils.deprecation import MiddlewareMixin
from  django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse

class  UserAuthMiddle(MiddlewareMixin):

    def process_request(self,request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user:login'))
        else:
            return HttpResponseRedirect(reverse('index'))