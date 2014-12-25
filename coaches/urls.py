from django.conf.urls import patterns, url

from coaches.views import Coaches, coach_info


urlpatterns = patterns('',
                       url(r'^/(?P<coach_id>\d+)/$', coach_info,
                           name="coach_info"),
                       url(r'^/$', Coaches.as_view(), name='coaches_list'),
                       )
