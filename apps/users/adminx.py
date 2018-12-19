#author_by zhuxiaoliang
#2018-12-10 下午2:21

from  .models import EmailVerifyRecord,UserProfile,Banner
import xadmin
from xadmin import views



class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']

# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '后台管理界面'
    # 修改footer
    site_footer = '未来网络高精尖中心'
    # 收起菜单
    menu_style = 'accordion'

# 将title和footer信息进行注册

xadmin.site.register(views.CommAdminView,GlobalSettings)


xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)