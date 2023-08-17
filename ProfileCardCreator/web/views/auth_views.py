from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group

from ProfileCardCreator.web.views.authorization import CustomLoginRequiredMixin


class IndexView(TemplateView):
    template_name = "index.html"


class RegisterView(FormView):
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        user_group = Group.objects.get(name='User_group')
        user.groups.add(user_group)
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'authentication/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(CustomLoginRequiredMixin, RedirectView):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


