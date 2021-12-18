from django import forms
from django.contrib.auth.forms import UserCreationForm

from theauth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        required=True
    )

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'
