from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from ProfileCardCreator.web.forms.task import TodoTaskForm
from ProfileCardCreator.web.models import TodoTask


class TasksListView(ListView):
    model = TodoTask
    template_name = "todo-task/task-list.html"
    context_object_name = "tasks"


class CreateTaskView(CreateView):
    model = TodoTask
    form_class = TodoTaskForm
    template_name = "todo-task/task-create.html"
    success_url = reverse_lazy('all tasks')

    def form_valid(self, form):
        form.instance.Creator = self.request.user
        return super().form_valid(form)