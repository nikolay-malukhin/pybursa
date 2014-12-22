from django.conf.urls import patterns, url

from students.views import student_info, students_list, student_edit, student_new, student_delete


urlpatterns = patterns('',
                       url(r'^/(?P<student_id>\d+)/$', student_info,
                           name="student_info"),
                       url(r'^/edit/(?P<student_id>\d+)/$', student_edit, name='student_edit'),
                       url(r'^/new/$', student_new, name='student_new'),
                       url(r'^/delete/(?P<student_id>\d+)/$', student_delete, name='student_delete'),
                       url(r'^/$', students_list, name='students_list'),
                       )
