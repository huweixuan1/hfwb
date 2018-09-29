from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BusnessTag(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.name



class BusnessInfo(models.Model):
    user = models.ForeignKey(User,related_name='busness',on_delete=models.CASCADE)
    name = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    tel = models.CharField(max_length=25,null=True,blank=True)
    industry = models.ForeignKey(BusnessTag,related_name='busness_info',on_delete=models.CASCADE)
    opentime = models.CharField(max_length=50,null=True,blank=True)
    detail = models.TextField()
    logoimg = models.CharField(max_length=100,null=True,blank=True)
    wximg = models.CharField(max_length=100,null=True,blank=True)
    busimg = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.name
