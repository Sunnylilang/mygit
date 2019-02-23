from django.db import models

# Create your models here.


class Positions(models.Model):
    company = models.CharField(max_length=100,null=False)
    position = models.CharField(max_length=100,null=False)
    salary = models.CharField(max_length=20,null=False)
    exprience = models.CharField(max_length=10,null=False)
    education = models.CharField(max_length=10,null=False)
    area = models.CharField(max_length=100,null=False)
    requirement = models.CharField(max_length=5000,null=False)
    trade = models.CharField(max_length=50,null=False)
    company_nature = models.CharField(max_length=20,null=False)
    scale = models.CharField(max_length=20,null=False)
    class Meta:
        db_table="zhaopin"
