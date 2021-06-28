from django import forms
from .models import Turf

class TurfCreateForm(forms.ModelForm):
    class Meta:
        model = Turf
        fields = '__all__'