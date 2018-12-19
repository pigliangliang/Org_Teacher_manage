#author_by zhuxiaoliang
#2018-12-06 下午8:58

class SVIPPermission(object):
    message='SVIP访问'

    def has_permission(self, request, view):
        if request.user.id==1:
            return True
        return False

class MyPremission(object):
    message='普通用户访问'
    def has_permission(self,request,view):
        if request.user.id  !=1 :
            return True
        return False