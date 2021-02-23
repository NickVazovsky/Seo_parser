from django import forms
from .models import SaveUrl


class SaveUrlForm(forms.ModelForm):
    class Meta:
        model = SaveUrl
        exclude = [""]
