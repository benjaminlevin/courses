from django.conf.urls import url
from . import views           # This line is new!

#models -- views -- templates

urlpatterns = [
  url(r'^$', views.index),
  url(r'^add$', views.add),
  url(r'^delete/(?P<id>\d+)$', views.delete),
  url(r'^courses/destroy/(?P<id>\d+)$', views.remove),
  url(r'^courses/comment/(?P<id>\d+)$', views.comment),
  url(r'^comment/(?P<id>\d+)$', views.addComment),
 ]