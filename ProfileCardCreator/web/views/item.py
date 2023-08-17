from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from ProfileCardCreator.web.forms.item import ItemForm
from ProfileCardCreator.web.models import Item
from ProfileCardCreator.web.views.authorization import SuperuserRequiredMixin, StuffRequiredMixin, \
    CustomLoginRequiredMixin


class ItemListView(CustomLoginRequiredMixin, ListView):
    model = Item
    template_name = 'item/item-list.html'
    context_object_name = 'items'


class ItemDetailView(CustomLoginRequiredMixin, DetailView):
    model = Item
    template_name = 'item/item-details.html'
    context_object_name = 'item'


class ItemCreateView(StuffRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/item-create.html'
    success_url = reverse_lazy('all items')


class ItemDeleteView(SuperuserRequiredMixin, View):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('all items')
