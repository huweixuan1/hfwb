


from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from wechat import views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'job/(?P<id>\d)',views.job,name='job'),
    url(r'house/(?P<id>\d)',views.house_base,name='house'),
    url(r'carpool/(?P<id>\d)',views.carpool,name='carpool'),
    url(r'oldcar',views.oldcar,name='oldcar'),
    url(r'olditem',views.olditem,name='olditem'),
    url(r'emergencyhelp',views.emergencyhelp,name='emergencyhelp'),
    url(r'lookforhelp',views.lookforhelp,name='lookforhelp'),
    url(r'lifeservice/(?P<id>\d)',views.lifeservice,name='lifeservice'),
    url(r'comment',views.comment,name='comment'),
    url(r'reply',views.reply,name='reply'),
    url(r'detail',views.detail,name='detail'),
    url(r'myself',views.myself,name='myself'),
    url(r'success',TemplateView.as_view(template_name='success.html'),name='success'),

    #url(r'ajax',views.ajax,name='ajax'),


    url(r'ceshi',views.ceshi,name='ceshi'),
]