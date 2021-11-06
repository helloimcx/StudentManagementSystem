# -*- coding: utf-8 -*-
from django import forms

from MainApp.models import StuInfo
from StudentMessage.models import StuBasicInfo

class StuForm(forms.ModelForm):
    class Meta:
        model = StuBasicInfo
        fields = ['photo','studentName','major','ClassName','sex','nation','hometown','political',
                  'idcard','eduBackground','englishlevel','bankcard','remarks']

class StuInfoForm(forms.ModelForm):
    class Meta:
        model = StuInfo
        fields = ['studentNo']
