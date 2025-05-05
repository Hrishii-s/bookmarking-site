from django import forms
from .models import Lists

class ListModelForm(forms.ModelForm):
    class Meta:
        model=Lists
        fields=["title","url"]
    