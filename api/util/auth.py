#author_by zhuxiaoliang
#2018-12-06 下午8:40

from api.models import UserToken,UserInfo
from rest_framework import exceptions


class Authentication(object):

    def authenticate(self,request):
        token = request._request.GET.get('token')
        print(token)
        token_obj = UserToken.objects.filter(token=token).first()

        if not token_obj:
            raise exceptions.AuthenticationFailed('认证失败')
        return (token_obj.user,token_obj)

    def get_authenticators(self):

        pass

    def get_authenticate_header(self, request):

        pass


    def authenticate_header(self,request):
        pass

