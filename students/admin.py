from django.contrib import admin

from students.models import Student, Dossier, Address


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Student, StudentAdmin)
admin.site.register(Address)
admin.site.register(Dossier)