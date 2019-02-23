from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):                           # 一个Model类将对应数据库中的一个表
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length= 20)
    phone = models.CharField(max_length=40)
    class Meta:
        db_table = "t_user"
