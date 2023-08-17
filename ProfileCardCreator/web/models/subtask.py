from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from .todo_task import TodoTask


class Subtask(models.Model):
    Title = models.CharField(null=False, max_length=30,
                             validators=[MaxLengthValidator(30), MinLengthValidator(2)])
    TodoTask = models.ForeignKey(TodoTask, on_delete=models.CASCADE)
