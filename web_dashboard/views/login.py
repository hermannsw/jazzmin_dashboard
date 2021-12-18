from django.contrib.auth import views
from django.shortcuts import redirect

from web_dashboard.forms.email_auth_form import EmailAuthenticationForm


class LoginView(views.LoginView):
    authentication_form = EmailAuthenticationForm

    def get_redirect_url(self):
        return self.request.GET.get(
            self.redirect_field_name,
            self.request.POST.get(self.redirect_field_name, '')
        )

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('web_dashboard:home')

        return super(LoginView, self).dispatch(request, *args, **kwargs)
