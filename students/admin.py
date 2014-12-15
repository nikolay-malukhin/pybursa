from django.contrib import admin

from students.models import Student, Dossier, Address


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'package')
    list_filtering = ('first_name', 'last_name', 'email', 'package')
    preserve_filters = True
    if Student.PACKAGE_CHOICES.__len__() < 5:
        radio_fields = {"package": admin.HORIZONTAL}
    filter_vertical = ['courses']

admin.site.register(Student, StudentAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house')
    list_filtering = ('zip', 'country', 'region', 'city', 'district', 'street')

admin.site.register(Address, AddressAdmin)


class DossierAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dossier, DossierAdmin)

