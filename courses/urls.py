from django.conf.urls import patterns, url

from courses.views import Courses, CourseEdit, CourseDelete, CourseAdd, CourseDetail


urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', CourseDetail.as_view(), name="course_info"),
                       url(r'^/edit/(?P<pk>\d+)/$', CourseEdit.as_view(), name='course_edit'),
                       url(r'^/new/$', CourseAdd.as_view(), name='course_new'),
                       url(r'^/delete/(?P<pk>\d+)/$', CourseDelete.as_view(), name='course_delete'),
                       url(r'^/$', Courses.as_view(), name='courses_list'),
                       )
