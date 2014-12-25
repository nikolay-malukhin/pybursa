from django.conf.urls import patterns, url

from courses.views import Courses, course_info, course_edit, course_delete, course_new


urlpatterns = patterns('',
                       url(r'^/(?P<course_id>\d+)/$', course_info,
                           name="course_info"),
                                              url(r'^/edit/(?P<course_id>\d+)/$', course_edit, name='course_edit'),
                       url(r'^/new/$', course_new, name='course_new'),
                       url(r'^/delete/(?P<course_id>\d+)/$', course_delete, name='course_delete'),
                       url(r'^/$', Courses.as_view(), name='courses_list'),
                       )
