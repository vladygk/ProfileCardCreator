from django import forms

from ProfileCardCreator.web.models import Subtask, TodoTask


class SubtaskForm(forms.ModelForm):
    TodoTask = forms.ModelChoiceField(queryset=TodoTask.objects.all(), empty_label=None)

    class Meta:
        model = Subtask
        fields = ['Title', 'TodoTask']
