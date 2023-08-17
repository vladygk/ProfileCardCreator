from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from .todo_task import TodoTask


class Item(models.Model):
    Name = models.CharField(null=False, max_length=30,
                            validators=[MaxLengthValidator(30), MinLengthValidator(2)])
    Price = models.IntegerField(null=False)
    ImageUrl = models.URLField(null=False)
    TodoTask = models.ForeignKey(TodoTask, on_delete=models.CASCADE)
