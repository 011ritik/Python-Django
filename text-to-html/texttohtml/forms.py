from django import forms
from .models import Parser
from ckeditor.widgets import CKEditorWidget

class ParserForm(forms.ModelForm):
    
    body = forms.CharField(widget=CKEditorWidget(), label="Text Editor")

    class Meta():
        model = Parser
        fields = "__all__"