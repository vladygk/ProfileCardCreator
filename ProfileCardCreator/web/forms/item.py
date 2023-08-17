from django import forms
from ProfileCardCreator.web.models import Item, TodoTask


class ItemForm(forms.ModelForm):
    TodoTask = forms.ModelChoiceField(queryset=TodoTask.objects.all(), empty_label=None)

    class Meta:
        model = Item
        fields = ['Name', 'Price', 'ImageUrl', 'TodoTask']
