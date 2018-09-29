from card.models import *
from django import forms

"""
CardInfo 名片表

"""

class CardInfoForm(forms.ModelForm):
    class Meta:
        model = CardInfo
        fields = ('name','tel','tag','wechatname','wechatimg','detail','position','sex')
