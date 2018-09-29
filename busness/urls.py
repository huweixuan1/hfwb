from django.conf.urls import url
from busness import views
urlpatterns = [
    url(r'createbusness',views.createbusness,name='createbusness'),
    url(r'post_img',views.post_img,name='post_img'),
    url(r'showbusness',views.showbusness,name='showbusness'),
    url(r'detail',views.detail,name='detail'),
]