from django.contrib import admin
from reports.models import Report
# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created', 'updated', )
    search_fields = ('name', 'author', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Report, ReportAdmin)
