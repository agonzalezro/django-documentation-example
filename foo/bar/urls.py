from django.conf.urls import patterns
from django.conf.urls import url

from bar import views

urlpatterns = patterns('',
    url(r'^$', views.index),
)
