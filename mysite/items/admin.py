from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Item, Category

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'item_slug': ('item_name',)}
    list_display = ('item_name', 'item_price', 'item_category', 'image_show')

    def image_show(self, obj):
        if obj.item_img:
            return mark_safe("<img src='{}' width='120' />".format(obj.item_img.url))
        return 'None'

    image_show.__name__ = 'Картинка'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'cat_slug': ('cat_name',)}

