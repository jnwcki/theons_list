from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView,\
     CreateAPIView, RetrieveAPIView
from theonsapp.forms import NewUserCreation
from theonsapp.models import Item, SubCategory, Category, City, UserProfile
from theonsapp.permissions import IsOwnerOrReadOnly
from theonsapp.serializers import CategorySerializer, SubCategorySerializer, \
    PostSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly


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
        if self.kwargs.get('ordering') == '1':
            context['item_list'] = Item.objects.filter(subcategory_id=self.kwargs.get('pk')).order_by("-time_listed")
        elif self.kwargs.get('ordering') == '2':
            context['item_list'] = Item.objects.filter(subcategory_id=self.kwargs.get('pk')).order_by("-price")
        elif self.kwargs.get('ordering') == '3':
            context['item_list'] = Item.objects.filter(subcategory_id=self.kwargs.get('pk')).order_by("price")
        return context


class ItemDetailView(DetailView):
    model = Item


class ListOfAPIViews(TemplateView):
    template_name = 'api_list.html'


class ListCategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ListSubCategoryAPIView(ListAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class ListPostSubCategoryAPIView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        captured_pk = self.kwargs['pk']
        return Item.objects.filter(subcategory_id=captured_pk)


class ListPostCategoryAPIView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        captured_pk = self.kwargs['pk']
        return Item.objects.filter(subcategory__category_id=captured_pk)


class DetailPostAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,
                          )
    queryset = Item.objects.all()


class CreatePostAPIView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Item.objects.all()
    permission_classes = (IsAuthenticated,)


class RetrieveCategoryAPIView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class RetrieveSubCategoryAPIView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = SubCategory.objects.all()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
