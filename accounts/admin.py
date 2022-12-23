from django.contrib import admin
from .models import User,UserProfile
from django.contrib.auth.admin import UserAdmin

class UserAdmin(admin.ModelAdmin):
    list_display=('email','first_name','last_name','username','role','is_active')

    filter_horizontal=()
    list_filter=()
    fieldsets=()
    readonly_fields=('password',)

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,UserAdmin)
admin.site.register(UserProfile,UserProfileAdmin)