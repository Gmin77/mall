from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class SignupForm(UserCreationForm):
    class Meta :
        model = User
        fields = ('name', 'email', 'password1', 'password2', 'user_image', 'real_name', 'phone_number', 'address', 'detail_address',)

class ProfileForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = ('name', 'real_name', 'phone_number', 'address', 'detail_address', 'user_image')
