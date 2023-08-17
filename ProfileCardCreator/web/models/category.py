from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class Category(models.Model):
    Name = models.CharField(null=False,  max_length=30,
                            validators=[MaxLengthValidator(30), MinLengthValidator(2)])
