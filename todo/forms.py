from django.forms import ModelForm
from .models import Todo
import numba


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
