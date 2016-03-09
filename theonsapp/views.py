from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView
from theonsapp.forms import NewUserCreation


class IndexView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    model = User
    form_class = NewUserCreation

    def form_valid(self, form):
        new_user = form.save()
        new_user_screen_name = form.cleaned_data.get('screen_name')
        new_user.userprofile.screen_name = new_user_screen_name
        new_user.userprofile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')
