"""theons_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from theons_list import settings
from theonsapp.views import IndexView, UserCreateView, CategoryDetailView, SubCategoryItemView, ItemDetailView, \
    MakeListingView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^accounts/login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout_then_login, name='logout'),
    url(r'^signup/', UserCreateView.as_view(), name='signup'),
    url(r'^media/(?P<path>.*)', "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
    url(r'^category/(?P<pk>\d+)', CategoryDetailView.as_view(), name="category_detail"),
    url(r'^subcategory/(?P<pk>\d+)/(?P<ordering>\d)', SubCategoryItemView.as_view(), name='sub_item_list'),
    url(r'^item_detail/(?P<pk>\d+)', ItemDetailView.as_view(), name='item_detail'),
    url(r'^create_listing/(?P<pk>\d+)', MakeListingView.as_view(), name='create_listing')
    ]
