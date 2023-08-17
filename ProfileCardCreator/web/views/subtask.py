from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from ProfileCardCreator.web.forms.subtask import SubtaskForm
from ProfileCardCreator.web.models import Subtask
from ProfileCardCreator.web.views.authorization import CustomLoginRequiredMixin, StuffRequiredMixin, \
    SuperuserRequiredMixin


class SubtaskListView(CustomLoginRequiredMixin, ListView):
    model = Subtask
    template_name = 'subtask/subtask-list.html'
    context_object_name = 'subtasks'


class SubtaskCreateView(StuffRequiredMixin, CreateView):
    model = Subtask
    form_class = SubtaskForm
    template_name = 'subtask/subtask-create.html'
    success_url = reverse_lazy('all subtasks')


class SubtaskDeleteView(SuperuserRequiredMixin, View):
    def get(self, request, pk):
        subtask = get_object_or_404(Subtask, pk=pk)
        subtask.delete()
        return redirect('all subtasks')
