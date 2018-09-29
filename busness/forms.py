from django import forms
from busness.models import *

class BusnessForm(forms.ModelForm):
    class Meta:
        model = BusnessInfo
        fields = ('name','address','tel','industry','opentime','detail','logoimg','wximg','busimg')
