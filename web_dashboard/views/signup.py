from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from web_dashboard.forms.signup import SignupForm


def form_render(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/admin')
    else:
        form = SignupForm()
    return render(request, 'web_dashboard/signup.html', {'form': form})
