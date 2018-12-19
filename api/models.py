from django.db import models

# Create your models here.

class UserInfo(models.Model):

    USER_TYPE= (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP')
    )

    usertype = models.IntegerField(choices=USER_TYPE,default=1)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.username


class UserToken(models.Model):
    user = models.OneToOneField(UserInfo,on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

    def __str__(self):
        return self.token