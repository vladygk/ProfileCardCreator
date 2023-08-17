from asgiref.sync import sync_to_async, async_to_sync
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
import asyncio
from ProfileCardCreator.web.forms import FieldOfWorkForm
from ProfileCardCreator.web.models import FieldOfWork
from ProfileCardCreator.web.views.authorization import CustomLoginRequiredMixin, StuffRequiredMixin, \
    SuperuserRequiredMixin


class FieldOfWorkListView( CustomLoginRequiredMixin,ListView):
    model = FieldOfWork
    template_name = 'field-of-work/field-of-work-list.html'
    context_object_name = 'fields'


class FieldOfWorkCreateView(StuffRequiredMixin, CreateView):
    model = FieldOfWork
    form_class = FieldOfWorkForm
    template_name = 'field-of-work/field-of-work-create.html'
    success_url = reverse_lazy('all fields')


class FieldOfWorkDeleteView(SuperuserRequiredMixin, View):
    def get(self, request, pk):
        field = get_object_or_404(FieldOfWork, pk=pk)
        field.delete()
        return redirect('all fields')
