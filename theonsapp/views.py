from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from theonsapp.forms import NewUserCreation
from theonsapp.models import Item, SubCategory, Category, City, UserProfile


class IndexView(ListView):
    template_name = 'index.html'
    model = Category


class UserCreateView(CreateView):
    model = User
    form_class = NewUserCreation

    def form_valid(self, form):
        user_object = form.save()
        city = form.cleaned_data.get("home_city")
        profile = UserProfile.objects.create(user=user_object, home_city=city)
        profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class MakeListingView(CreateView):
    model = Item
    fields = ['name', 'full_description', 'photo', 'price']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.subcategory = SubCategory.objects.get(pk=self.kwargs.get('pk'))

        user_profile = UserProfile.objects.get(user=self.request.user)
        post.location = City.objects.get(pk=user_profile.home_city.pk)
        post.seller_id = user_profile.user.pk
        print(user_profile)
        post.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        return reverse('index')


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs.get('pk'))
        return context


class SubCategoryItemView(ListView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.get(pk=self.kwargs.get('pk'))
        #print(ordering)
        print(self.kwargs.get('ordering', 1))
        if self.kwargs.get('ordering') == '1':
            context['item_list'] = Item.objects.filter(subcategory_id=self.kwargs.get('pk')).order_by("-time_listed")
        elif self.kwargs.get('ordering') == '2':
            context['item_list'] = Item.objects.filter(subcategory_id=self.kwargs.get('pk')).order_by("-price")
        elif self.kwargs.get('ordering') == '3':
            context['item_list'] = Item.objects.filter(subcategory_id=self.kwargs.get('pk')).order_by("price")
        print(context)
        return context


class ItemDetailView(DetailView):
    model = Item
