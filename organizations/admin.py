from django.contrib import admin
from .models import Organization, Project

class OrganizationAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Project)
