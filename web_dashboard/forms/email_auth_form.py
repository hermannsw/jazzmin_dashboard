from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _("Email")})
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': _("Password")}),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(email)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        self.user_cache = authenticate(self.request, email=email, password=password)
        if self.user_cache is None:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'email': email},
            )
        else:
            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        pass

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
