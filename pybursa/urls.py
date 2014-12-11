from django.views.generic import TemplateView

from django.conf.urls import patterns, include, url
from django.contrib import admin
from students.views import address_info, address_list, dossier_list

urlpatterns = patterns('',
                       url(r'^student', include('students.urls')),
                       url(r'^address/', address_list, name="address_list"),
                       url(r'^dossier/', dossier_list, name="dossier_list"),
                       url(r'^coach', include('coaches.urls')),
                       url(r'^course', include('courses.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$',
                           TemplateView.as_view(template_name='index.html'),
                           name='index'),
)
