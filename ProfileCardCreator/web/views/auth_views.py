from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import FormView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page upon successful registration

    def form_valid(self, form):
        # This method is called when the form is valid
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')  # Redirect to home page upon successful login

    def form_valid(self, form):
        # This method is called when the form is valid
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('index')  # Redirect to home page upon logout

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
