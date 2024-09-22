from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import RegisterForm, LoginForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'login_form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")
