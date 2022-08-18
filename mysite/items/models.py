from django.db import models
from django.urls import reverse


class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='category')
    cat_slug = models.SlugField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.cat_name




class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_slug = models.SlugField(max_length=20, null=True, blank=True)
    item_desc = models.CharField(max_length=200)
    item_price = models.CharField(max_length=10)
    item_img = models.ImageField(upload_to='media/itemimg/')
    item_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('post', kwargs={'item_slug': self.item_slug})

