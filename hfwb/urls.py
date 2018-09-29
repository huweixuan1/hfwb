"""hfwb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #初始设置，验证token，信息自动回复
    url(r'index/',views.index),
    #url(r'',TemplateView.as_view(template_name='MP_verify_1b5lJAphbOGco59t.txt')),
    #创建自定义菜单，点击后可跳转到指定页面
    url(r'create_ms',views.create_ms),
    #主页面
    url(r'home',views.home,name='home'),
    url(r'^create$',TemplateView.as_view(template_name="create.html"),name='create'),
    #授权微信页面
    url(r'userinfo',views.userinfo),
    url(r'^wechat/',include(('wechat.urls','wechat'),namespace ='wechat')),
    url(r'^card/',include(('card.urls','card'),namespace ='card')),
    url(r'^busness/',include(('busness.urls','busness'),namespace ='busness')),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
