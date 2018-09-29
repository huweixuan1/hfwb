from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

#个人名片标签
class CardTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CardInfo(models.Model):
    user = models.OneToOneField(User,related_name='card',on_delete=models.CASCADE)
    name = models.CharField(max_length=20,null=True,blank=True)
    sex = models.CharField(max_length=10,null=True,blank=True)
    tel = models.CharField(max_length=30,null=True,blank=True)
    tag = models.CharField(max_length=30,null=True,blank=True)
    wechatname = models.CharField(max_length=30,null=True,blank=True)
    wechatimg = models.FileField()
    detail = models.TextField(null=True,blank=True)
    position = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name



