from django.conf.urls import url
from card import views
urlpatterns = [
    url(r'cardcreate',views.creatcard,name='cardcreate'),
    url(r'cardlist',views.cardlist,name='cardlist'),
    url(r'carddetail',views.carddetail,name='carddetail'),
]