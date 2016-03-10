from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from theonsapp.forms import NewUserCreation
from theonsapp.models import Item, SubCategory, Category


class IndexView(ListView):
    template_name = 'index.html'
    model = Category

class UserCreateView(CreateView):
    model = User
    form_class = NewUserCreation

    #def form_valid(self, form):
        #new_user = form.save()
        #new_user_screen_name = form.cleaned_data.get('screen_name')
        #new_user.userprofile.screen_name = new_user_screen_name
        #new_user.userprofile.save()
        #return super().form_valid(form)
        #pass

    def get_success_url(self):
        return reverse('login')


class MakeListingView(CreateView):
    model = Item
    fields = ['name', 'full_description']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.sub_category = SubCategory.objects.get(pk=self.kwargs.get(subcategory_id))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.get(pk=self.kwargs.get(subcategory_id))
        return context


class CategoryListView(ListView):
    model = Category

