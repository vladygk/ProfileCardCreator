from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from .field_of_work import FieldOfWork
from django.contrib.auth.models import User


class TodoTask(models.Model):
    Title = models.CharField(null=False, max_length=30,
                             validators=[MaxLengthValidator(30), MinLengthValidator(2),
                                         RegexValidator(r'^[A-Za-z ]+$',
                                                        message="Todo task name should contain only letters!")])
    Description = models.CharField(null=False, max_length=30,
                                   validators=[MaxLengthValidator(30), MinLengthValidator(2), ])
    Deadline = models.DateField(null=False)
    IsCompleted = models.BooleanField()
    FieldOfWork = models.ForeignKey(FieldOfWork, on_delete=models.CASCADE)
    Creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    Assignee = models.ForeignKey(User, related_name='assignee', on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
