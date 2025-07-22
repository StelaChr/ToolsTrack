from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from accounts.forms import AppUserCreationForm

UserModel = get_user_model()


# Create your views here.
class RegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name ='register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        if response.status_code in [301, 302]:
            login(self.request, self.object)

        return response


