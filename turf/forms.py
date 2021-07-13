from django import forms
from .models import Turf

class TurfCreateForm(forms.ModelForm):
    class Meta:
        model = Turf
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(TurfCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
class TurfUpdateForm(forms.ModelForm):
    class Meta:
        model = Turf
        fields = ['name','place','price']