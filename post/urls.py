
from django.urls import path,URLPattern
from .views import *
from django.conf.urls import url

app_name="blog_post_app_name"

urlpatterns = [
    url('index/', postIndex, name="anasayfa"),
    url(r'^(?P<pk>[0-9]+)$', postDetail, name="detay"),
    url(r'^(?P<pk>[0-9]+)/update/$', postUpdate, name="guncelle"),
    url(r"^(?P<pk>[0-9]+)/delete/$", postDelete, name="silme"),
    url('create/', post_create, name="postCreated"),
]
