from django import forms

from . import models

class CreatePersoneForm(forms.ModelForm):
    phones = forms.CharField(widget = forms.Textarea(), help_text="Введите с новой строки.'\\n'")
    class Meta:
        model =models.Persone
        fields = (
            'name',
            'phones'
        )
