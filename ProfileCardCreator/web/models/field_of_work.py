from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from .category import Category


class FieldOfWork (models.Model):
    Name = models.CharField(null=False,max_length=30,
                            validators=[MaxLengthValidator(30), MinLengthValidator(2)])
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
