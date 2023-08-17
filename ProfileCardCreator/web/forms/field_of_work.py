from django import forms
from ProfileCardCreator.web.models import FieldOfWork,Category


class FieldOfWorkForm(forms.ModelForm):
    Category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    class Meta:
        model = FieldOfWork
        fields = ['Name', 'Category']
