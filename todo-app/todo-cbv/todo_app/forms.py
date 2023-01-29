from .models import TodoModel
from django import forms

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = TodoModel
        fields = '__all__'