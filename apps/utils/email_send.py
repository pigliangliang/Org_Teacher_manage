#author_by zhuxiaoliang
#2018-12-10 下午7:30

"xjqgdwtdkvoybcgh"
from datetime import datetime

# apps/utils/email_send.py

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from untitled1.settings import EMAIL_FROM

# 生成随机字符串
def random_str(random_length=8):
    str = ''
    # 生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str

# 发送注册邮件
def send_register_eamil(email, send_type="找回密码"):
    # 发送之前先保存到数据库，到时候查询链接是否存在
    # 实例化一个EmailVerifyRecord对象
    email_record = EmailVerifyRecord()
    # 生成随机的code放入链接
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.send_time = datetime.now()
    email_record.save()

    # 定义邮件内容:
    email_title = ""
    email_body = ""


    email_title = "链接"
    email_body = "请点击下面连接重置密码: http://127.0.0.1:8080/reset/{0}/".format(code)

    # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，发件人邮箱地址，收件人（是一个字符串列表）
    send_mail(email_title, email_body, EMAIL_FROM, [EMAIL_FROM,])
    # 如果发送成功
