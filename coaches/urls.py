from django.conf.urls import patterns, url

from coaches.views import Coaches, CoachDetail, CoachAdd, CoachEdit, CoachDelete


urlpatterns = patterns('',
                       url(r'^/(?P<pk>\d+)/$', CoachDetail.as_view(), name="coach_info"),
                       url(r'^/$', Coaches.as_view(), name='coaches_list'),
                       url(r'^add/$', CoachAdd.as_view(), name="coach_add"),
                       url(r'^edit/(?P<pk>\d+)/$', CoachEdit.as_view(), name="coach_edit"),
                       url(r'^delete/(?P<pk>\d+)/$', CoachDelete.as_view(), name="coach_delete"),
                       )
