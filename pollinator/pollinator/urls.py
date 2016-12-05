from django.conf.urls import url
from django.contrib import admin
from polls import views

urlpatterns = [
	url(r'^polls/$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^polls/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^polls/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^polls/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
