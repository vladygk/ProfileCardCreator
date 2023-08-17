from django import forms
from django.contrib.auth.models import User

from ProfileCardCreator.web.models import TodoTask, FieldOfWork


class TodoTaskForm(forms.ModelForm):
    FieldOfWork = forms.ModelChoiceField(queryset=FieldOfWork.objects.all(), empty_label=None)
    Assignee = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)

    class Meta:
        model = TodoTask
        fields = ['Title', 'Description', 'Deadline', 'FieldOfWork','Assignee','IsCompleted']
        widgets = {
            'Deadline': forms.DateInput(attrs={'type': 'date'}),
            'IsCompleted':forms.CheckboxInput()
        }
