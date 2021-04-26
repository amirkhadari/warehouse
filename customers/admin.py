from django.contrib import admin
from .models import Customer
# Register your models here.


# admin.site.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Customer, CustomerAdmin)
