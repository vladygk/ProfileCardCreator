from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from ProfileCardCreator.web.forms.item import ItemForm
from ProfileCardCreator.web.models import Item


class ItemListView(ListView):
    model = Item
    template_name = 'item/item-list.html'
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/item-details.html'
    context_object_name = 'item'


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/item-create.html'
    success_url = reverse_lazy('all items')


class ItemDeleteView(View):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('all items')
