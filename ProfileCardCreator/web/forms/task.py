from django import forms
from ProfileCardCreator.web.models import TodoTask, FieldOfWork


class TodoTaskForm(forms.ModelForm):
    FieldOfWork = forms.ModelChoiceField(queryset=FieldOfWork.objects.all(), empty_label=None)

    class Meta:
        model = TodoTask
        fields = ['Title', 'Description', 'Deadline', 'FieldOfWork']
        widgets = {
            'Deadline': forms.DateInput(attrs={'type': 'date'}),
        }
