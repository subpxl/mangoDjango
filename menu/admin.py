from django.contrib import admin
from .models import Category, Product, Strain, Unit
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'vendor', 'updated_at')
    search_fields = ('category_name', 'vendor__vendor_name ')


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_title',)}
    list_display = ('product_title', 'category', 'vendor',
                    'price', 'is_available', 'updated_at',)
    search_fields = ('product_title', 'category__category_name',
                     'vendor__vendor_name', 'price',)


class StrainAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Unit)
admin.site.register(Strain, StrainAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
