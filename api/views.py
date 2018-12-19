from .models import UserToken,UserInfo
from django.http import JsonResponse
from rest_framework.views import APIView
from api.util.auth import Authentication
from api.util.permission import MyPremission


# Create your views here.


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))

    return m.hexdigest()


class AuthView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request,*args,**kwargs):
        username = request._request.POST.get('username')
        password = request._request.POST.get('password')
        print(username,password)
        obj = UserInfo.objects.filter(username=username,password=password).first()
        if not obj:

            UserInfo.objects.create(username=username,password=password)
        token = md5(username)

        UserToken.objects.update_or_create(user=obj,defaults={'token':token})
        return JsonResponse({'token':token})



order_info = {
            'id': '001',
            'info': 'banana',
        }

class OrderView(APIView):

    authentication_classes = [Authentication,]
    permission_classes = []
    def get(self,request):

        return  JsonResponse('general',safe=False)

class VipOrderView(APIView):
    def get(self):
        return JsonResponse('vip')