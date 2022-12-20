from django.contrib import admin
from .models import User,UserProfile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('email','first_name','last_name','username','role','is_admin')
    filter_horizontal=()
    list_filter=()
    fieldsets=()

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,UserAdmin)
admin.site.register(UserProfile,UserProfileAdmin)