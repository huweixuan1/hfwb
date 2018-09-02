

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

"""
Total       #信息总表
JobInfo		# 求职招聘表
JobTag  #求职招聘标签表
House_Trade #房屋租售信息表

Carpool #顺风拼车表
OldCar #二手车辆表
OldItem #二手物品
LifeService #生活服务表
EmergencyHelp #紧急求助信息表
LookFor #寻人寻物信息表






CREATE DATABASE itcast_wechat DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
"""




class UserInfo(models.Model):
    user = models.OneToOneField(User,related_name='userinfo',unique=True,on_delete=models.CASCADE)
    openid = models.CharField(max_length=50,blank=True)
    sex = models.IntegerField(blank=True)
    province = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=20,blank=True)
    headimgurl = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

class JobTag(models.Model):
    tag = models.CharField(max_length=20)


    def __str__(self):
        return self.tag


class JobInfo(models.Model):
    user = models.ForeignKey(User,related_name='jobinfo',on_delete=models.CASCADE)
    type = models.IntegerField(blank=True)
    content = models.TextField()
    contact = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    requre = models.ManyToManyField(JobTag,related_name='jobtag',blank=True)
    img = models.CharField(max_length=200,null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class HouseTag(models.Model):
    tag = models.CharField(max_length=20)


    def __str__(self):
        return self.tag


class House_Trade(models.Model):
    type = models.CharField(max_length=20,blank=True)
    user = models.ForeignKey(User,related_name='housemsg',on_delete=models.CASCADE)
    position = models.CharField(max_length=50,blank=True)
    housetype = models.CharField(max_length=50,blank=True)
    area = models.CharField(max_length=20,blank=True)
    price = models.CharField(max_length=20,blank=True)
    detail = models.TextField()
    img = models.CharField(max_length=200,null=True, blank=True)
    tag = models.ManyToManyField(HouseTag,related_name='house',blank=True)
    contact = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.detail

class CarpoolTag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class CarPool(models.Model):
    user = models.ForeignKey(User,related_name="carpool",on_delete=models.CASCADE)
    type = models.CharField(max_length=10,blank=True)
    beginning = models.CharField(max_length=30,blank=True)
    destination = models.CharField(max_length=30,blank=True)
    begin_time = models.CharField(max_length=20,blank=True)
    seat = models.CharField(max_length=10,blank=True,null=True)
    isfee = models.CharField(max_length=10,blank=True)
    detail = models.TextField()
    img = models.CharField(max_length=200,null=True, blank=True)
    tag = models.ManyToManyField(CarpoolTag,related_name='carpool',blank=True)
    contact = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.beginning+'-->'+self.destination



class OldCar(models.Model):
    user = models.ForeignKey(User,related_name='oldcar',on_delete=models.CASCADE)
    brand = models.CharField(max_length=20,blank=True)
    carsystem = models.CharField(max_length=20,blank=True)
    carmodel = models.CharField(max_length=20,blank=True)
    price = models.CharField(max_length=20,blank=True)
    car_age = models.CharField(max_length=20,blank=True)
    distance = models.CharField(max_length=20,blank=True)
    detail = models.TextField()
    img = models.CharField(max_length=200,null=True, blank=True)
    contact = models.CharField(max_length=20,blank=True)
    tel = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand+self.carsystem


class OldItem(models.Model):
    user = models.ForeignKey(User,related_name='olditem',on_delete=models.CASCADE)
    goods = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    detail = models.TextField()
    img = models.CharField(max_length=200,null=True, blank=True)
    contact = models.CharField(max_length=20, blank=True)
    tel = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.goods


class LifeService(models.Model):
    user = models.ForeignKey(User, related_name='lifeservice', on_delete=models.CASCADE)
    type = models.CharField(max_length=10,blank=True)
    detail = models.TextField()
    img = models.CharField(max_length=200,null=True, blank=True)
    contact = models.CharField(max_length=20, blank=True)
    tel = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.detail


class EmergencyHelp(models.Model):
    user = models.ForeignKey(User, related_name='emehelp', on_delete=models.CASCADE)

    detail = models.TextField()
    img = models.CharField(max_length=200,null=True, blank=True)
    contact = models.CharField(max_length=20, blank=True)
    tel = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.detail


class LookForHelp(models.Model):
    user = models.ForeignKey(User, related_name='lookhelp', on_delete=models.CASCADE)

    detail = models.TextField()
    img = models.CharField(max_length=200,null=True, blank=True)
    contact = models.CharField(max_length=20, blank=True)
    tel = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.detail



class Total(models.Model):
    job = models.OneToOneField("jobinfo",blank=True,null=True,on_delete=models.CASCADE)
    house = models.OneToOneField('House_Trade',blank=True,null=True,on_delete=models.CASCADE)
    look_help = models.OneToOneField("LookForHelp",blank=True,null=True,on_delete=models.CASCADE)
    eme_help = models.OneToOneField('EmergencyHelp',  blank=True, null=True, on_delete=models.CASCADE)
    life_ser = models.OneToOneField('LifeService',  blank=True, null=True,
                                 on_delete=models.CASCADE)
    old_item = models.OneToOneField('OldItem', blank=True, null=True,
                                     on_delete=models.CASCADE)
    old_car = models.OneToOneField('OldCar',  blank=True, null=True,
                                    on_delete=models.CASCADE)
    car_pool = models.OneToOneField('CarPool',  blank=True, null=True,
                                    on_delete=models.CASCADE)


    time = models.DateTimeField(default=timezone.now)
    img = models.CharField(max_length=200,blank=True,null=True)


    def save(self, *args,**kwargs):
        try:
            self.job.created
            self.img = self.job.img
            self.time = self.job.created
        except:
            try:
                self.house.created
                self.img = self.house.img
                self.time = self.house.created
            except:
                try:
                    self.look_help.created
                    self.img = self.look_help.img
                    self.time = self.look_help.created
                except:
                    try:
                        self.eme_help.created
                        self.img = self.eme_help.img
                        self.time = self.eme_help.created

                    except:
                        try:
                            self.life_ser.created
                            self.img = self.life_ser.img
                            self.time = self.life_ser.created
                        except:
                            try:
                                self.old_item.created
                                self.img = self.old_item.img
                                self.time =self.old_item.created
                            except:
                                try:
                                    self.old_car.created
                                    self.img = self.old_car.img
                                    self.time= self.old_car.created
                                except:
                                    try:
                                        self.car_pool.created
                                        self.img =self.car_pool.img
                                        self.time = self.car_pool.created
                                    except:
                                        pass


        super(Total,self).save(*args,**kwargs)





class Images(models.Model):
    img = models.FileField(null=True,blank=True)




class Comments(models.Model):
    belong_article = models.ForeignKey(Total,related_name="comment",on_delete=models.CASCADE)
    belong_user = models.ForeignKey(User,related_name="com_user",on_delete=models.CASCADE)
    words = models.CharField(max_length=100,null=False)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.belong_user.username + ":"+self.words

class Reply(models.Model):
    belong_article = models.ForeignKey(Total,related_name='reply',on_delete=models.CASCADE)
    belong_user = models.ForeignKey(User, related_name="repy_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
    words = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.belong_user.username + '回复' + self.to_user.username +':'+self.words



