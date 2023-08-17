from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from .field_of_work import FieldOfWork
from django.contrib.auth.models import User


class TodoTask(models.Model):
    Title = models.CharField(null=False, max_length=30,
                             validators=[MaxLengthValidator(30), MinLengthValidator(2),
                                         RegexValidator(r'^[A-Za-z]+$',
                                                        message="Todo task name should contain only letters!")])
    Description = models.TextField(null=False)
    Deadline = models.DateField(null=False)
    FieldOfWork = models.ForeignKey(FieldOfWork, on_delete=models.CASCADE)
    Creator = models.ForeignKey(User, on_delete=models.CASCADE)
