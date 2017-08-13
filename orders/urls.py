from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'select', views.select, name='select'),
    url(r'list', views.orderList, name='list'),
]