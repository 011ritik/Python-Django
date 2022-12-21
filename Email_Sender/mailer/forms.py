from django import forms

class EmailSender(forms.Form):
    to = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(max_length=2500)