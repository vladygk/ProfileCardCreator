from django import forms
from ProfileCardCreator.web.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Name']
