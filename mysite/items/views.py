from django.shortcuts import render
from .models import Item
from django.views.generic import DetailView

def main_page(request):
    furniture_list = Item.objects.all()
    object_list = {
        'f_list': furniture_list,
    }
    return render(request, 'index.html', object_list)

class ItemDetail(DetailView):
    model = Item
    template_name = 'details.html'
    context_object_name = 'item_details'
