from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, FormView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth import login
# Create your views here.


class Login(LoginView):
    model = User
    template_name = "login/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("index")


class Register(CreateView):
    model = User
    template_name = "login/register.html"
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("index")
        return super(Register, self).get(*args, **kwargs)


