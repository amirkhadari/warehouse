from django.contrib import admin
from profiles.models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_user_name', 'created_on', 'updated_on')
    search_fields = ('get_user_name', )


admin.site.register(Profile, ProfileAdmin)
