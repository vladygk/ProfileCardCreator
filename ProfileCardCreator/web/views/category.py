from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from ProfileCardCreator.web.forms import CategoryForm
from ProfileCardCreator.web.models import Category
from django.views.generic import ListView

from ProfileCardCreator.web.views.authorization import CustomLoginRequiredMixin, SuperuserRequiredMixin, \
    StuffRequiredMixin


class CategoryListView(CustomLoginRequiredMixin, ListView):
    model = Category
    template_name = 'category/category-list.html'
    context_object_name = 'categories'


class CategoryCreateView(StuffRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category-create.html'
    success_url = reverse_lazy('all categories')


class CategoryDeleteView(SuperuserRequiredMixin, View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect('all categories')
