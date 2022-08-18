from django.shortcuts import render, get_object_or_404
from .models import Item, Category

def main_page(request, category_slug=None):

    furniture_list = Item.objects.all()
    categories = Category.objects.all()
    if category_slug:
        furniture_list = Item.objects.filter(item_category__cat_slug=category_slug)
    object_list = {
        'f_list': furniture_list,
        'categories': categories,
    }
    return render(request, 'index.html', object_list)

def item_detail(request, slug):
    product = Item.objects.filter(item_slug=slug).first()
    return render(request, 'details.html', {'product': product})
