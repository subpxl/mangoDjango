from django.contrib import admin
from .models import Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'fooditem', 'quantity')


admin.site.register(Cart)
