from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^$', views.hello, name='hello'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/delete$',views.post_delete, name='post_delete'),
	url(r'^login', 'django.contrib.auth.views.login', name='login', kwargs={'template_name':'post_loginform.html'}),
	url(r'^logout', 'django.contrib.auth.views.logout', name='logout'),
]
