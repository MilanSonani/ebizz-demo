from django import forms
from .models import Todo


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'category', 'is_completed']
