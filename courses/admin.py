from django.contrib import admin

# Register your models here.
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'technology', 'start_date', 'end_date')
    list_filtering = ('name', 'technology', 'start_date', 'end_date')
    prepopulated_fields = {"slug": ("name",)}
    if Course.TECHNOLOGY_CHOICE.__len__() < 5:
        radio_fields = {"technology": admin.HORIZONTAL}


admin.site.register(Course, CourseAdmin)