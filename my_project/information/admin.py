from django.contrib import admin
from information.models import Information, Section


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')


class InformationAdmin(admin.ModelAdmin):
    list_display = ('section', 'title', 'details', 'status')


admin.site.register(Information, InformationAdmin)
admin.site.register(Section, SectionAdmin)
