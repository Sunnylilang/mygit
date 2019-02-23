from django.db import models

# Create your models here.
class User(models.Model):
    password=models.CharField(max_length=30)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=20)
    status=models.CharField(max_length=5)
    class Meta:
        # managed = False
        db_table = 't_user'