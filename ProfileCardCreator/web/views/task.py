from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from ProfileCardCreator.web.forms.task import TodoTaskForm
from ProfileCardCreator.web.models import TodoTask
from ProfileCardCreator.web.views.authorization import CustomLoginRequiredMixin, StuffRequiredMixin, \
    SuperuserRequiredMixin


class TasksListView(CustomLoginRequiredMixin, ListView):
    model = TodoTask
    template_name = "todo-task/task-list.html"
    context_object_name = "tasks"
    ordering = ["-created_at"]


class CreateTaskView(StuffRequiredMixin, CreateView):
    model = TodoTask
    form_class = TodoTaskForm
    template_name = "todo-task/task-create.html"
    success_url = reverse_lazy('all tasks')

    def form_valid(self, form):
        form.instance.Creator = self.request.user
        form.instance.IsCompleted = False
        return super().form_valid(form)


class TaskDeleteView(SuperuserRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(TodoTask, pk=pk)
        task.delete()
        return redirect('all tasks')


class TaskMarkAsDoneView(StuffRequiredMixin, View):
    def get(self, request, pk):
        task = TodoTask.objects.get(pk=pk)
        task.IsCompleted = True
        task.save()
        return redirect('all tasks')


class TodoTaskUpdateView(StuffRequiredMixin, UpdateView):
    model = TodoTask
    fields = ['Title', 'Description', 'Deadline', 'IsCompleted', 'FieldOfWork', 'Assignee']
    template_name = 'todo-task/task-edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):

        form.instance.Creator = self.request.user
        form.instance.IsCompleted = TodoTask.objects.get(pk=form.instance.pk).IsCompleted
        self.object.save()

        print(self.object)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('all tasks')
