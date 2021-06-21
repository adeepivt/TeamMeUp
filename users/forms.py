from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == 'password1':
                visible.field.widget.attrs['placeholder'] = 'password'
            elif visible.name == 'password2':
                visible.field.widget.attrs['placeholder'] = 'confirm Password'
            else:
                visible.field.widget.attrs['placeholder'] = visible.name

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile','location','img']


class VendorLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(VendorLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.name