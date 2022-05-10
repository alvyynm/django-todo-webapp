from .models import Task

from django import forms

class ToDoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'task_due_date', 'task_priority']