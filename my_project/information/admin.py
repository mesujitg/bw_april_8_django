from django.contrib import admin
from information.models import Information


class InformationAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'status')


admin.site.register(Information, InformationAdmin)


