from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Item, Category

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_price', 'item_category', 'item_img')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'cat_slug': ('cat_name',)}

