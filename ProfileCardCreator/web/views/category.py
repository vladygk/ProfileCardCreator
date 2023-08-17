from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from ProfileCardCreator.web.forms import CategoryForm
from ProfileCardCreator.web.models import Category

from django.views.generic import ListView


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category-list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category-create.html'
    success_url = reverse_lazy('all categories')
