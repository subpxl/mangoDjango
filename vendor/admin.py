from django.contrib import admin
from .models import Vendor, Links
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_name', 'is_approved', 'created_at')
    list_display_links = ('user', 'vendor_name')
    prepopulated_fields = {'vendor_name': ('vendor_slug',)}


admin.site.register(Vendor, VendorAdmin)
admin.site.register(Links)
