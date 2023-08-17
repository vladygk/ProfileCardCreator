from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from ProfileCardCreator.web.forms import FieldOfWorkForm
from ProfileCardCreator.web.models import FieldOfWork


class FieldOfWorkListView(ListView):
    model = FieldOfWork
    template_name = 'field-of-work/field-of-work-list.html'
    context_object_name = 'fields'


class FieldOfWorkCreateView(CreateView):
    model = FieldOfWork
    form_class = FieldOfWorkForm
    template_name = 'field-of-work/field-of-work-create.html'
    success_url = reverse_lazy('all fields')


