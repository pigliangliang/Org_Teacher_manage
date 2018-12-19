#author_by zhuxiaoliang
#2018-12-06 下午9:26

from rest_framework.throttling import BaseThrottle
import time
VISIT_RECORD = {}   #保存访问记录

class VisitThrottle(BaseThrottle):
    '''60s内只能访问3次'''
    def __init__(self):
        self.history = None   #初始化访问记录

    def allow_request(self,request,view):
        #获取用户ip (get_ident)
        remote_addr = self.get_ident(request)
        ctime = time.time()
        #如果当前IP不在访问记录里面，就添加到记录
        if remote_addr not in VISIT_RECORD:
            VISIT_RECORD[remote_addr] = [ctime,]     #键值对的形式保存
            return True    #True表示可以访问
        #获取当前ip的历史访问记录
        history = VISIT_RECORD.get(remote_addr)
        #初始化访问记录
        self.history = history

        #如果有历史访问记录，并且最早一次的访问记录离当前时间超过60s，就删除最早的那个访问记录，
        #只要为True，就一直循环删除最早的一次访问记录
        while history and history[-1] < ctime - 60:
            history.pop()
        #如果访问记录不超过三次，就把当前的访问记录插到第一个位置（pop删除最后一个）
        if len(history) < 3:
            history.insert(0,ctime)
            return True

    def wait(self):
        '''还需要等多久才能访问'''
        ctime = time.time()
        return 60 - (ctime - self.history[-1])