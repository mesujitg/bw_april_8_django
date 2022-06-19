from django.contrib import admin
from organizations.models import Organization


class OrgAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'type', 'status')


admin.site.register(Organization, OrgAdmin)
