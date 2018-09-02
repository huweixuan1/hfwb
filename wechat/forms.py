from django import forms
from wechat.models import *




"""
Total       #信息总表
JobInfo		# 求职招聘表
JobTag  #求职招聘标签表
House_Trade #房屋租售信息表


CREATE DATABASE itcast_wechat DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
"""

class JobInfoForm(forms.ModelForm):
    class Meta:
        model=JobInfo
        fields = ("type",'content','contact','tel','img',"requre")

class House_TradeForm(forms.ModelForm):
    class Meta:
        model = House_Trade
        fields = ("type","position","housetype","area","price","detail","img","tag","contact","tel")


class CarPoolForm(forms.ModelForm):
    class Meta:
        model = CarPool
        fields = ("type","beginning","destination","begin_time","seat","isfee","detail","img","tag","contact","tel")


class OldCarForm(forms.ModelForm):
    class Meta:
        model = OldCar
        fields = ("brand","carsystem","carmodel","price","car_age","distance","detail","img","contact","tel")

class OldItemForm(forms.ModelForm):
    class Meta:
        model = OldItem
        fields = ("goods","price","detail","img","contact","tel")

class LifeServiceForm(forms.ModelForm):
    class Meta:
        model = LifeService
        fields = ("detail","img","contact","tel")

class EmergencyHelpForm(forms.ModelForm):
    class Meta:
        model = EmergencyHelp
        fields = ("detail","img","contact","tel")

class LookForHelpForm(forms.ModelForm):
    class Meta:
        model = LookForHelp
        fields = ("detail","img","contact","tel")
class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ("img",)