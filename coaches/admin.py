from django.contrib import admin

# Register your models here.
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'type')
    list_filtering = ('first_name', 'last_name', 'type')
    if Coach.COACH_TYPES.__len__() < 5:
        radio_fields = {"type": admin.HORIZONTAL}

admin.site.register(Coach, CoachAdmin)