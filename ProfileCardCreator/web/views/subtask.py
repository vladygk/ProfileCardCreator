from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from ProfileCardCreator.web.forms.subtask import SubtaskForm
from ProfileCardCreator.web.models import Subtask


class SubtaskListView(ListView):
    model = Subtask
    template_name = 'subtask/subtask-list.html'
    context_object_name = 'subtasks'


class SubtaskCreateView(CreateView):
    model = Subtask
    form_class = SubtaskForm
    template_name = 'subtask/subtask-create.html'
    success_url = reverse_lazy('all subtasks')
