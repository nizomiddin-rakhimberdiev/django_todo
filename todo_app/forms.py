from django import forms

from todo_app.models import Task


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

