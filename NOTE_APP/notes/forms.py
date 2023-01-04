from .models import Notes
from django import forms

class NoteFormView(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea()
        }