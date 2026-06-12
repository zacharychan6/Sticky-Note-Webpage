from django import forms
from .models import sticky_note


class StickyForm(forms.ModelForm):
    class Meta:
        model = sticky_note
        fields = ['title', 'content']
