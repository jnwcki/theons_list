from django.conf.urls import url
from django.contrib import admin
from theons_list import settings
from theonsapp.views import IndexView, UserCreateView, CategoryDetailView, \
                            SubCategoryItemView, ItemDetailView, \
                            MakeListingView, ListCategoryAPIView, \
                            ListSubCategoryAPIView, \
                            ListPostSubCategoryAPIView, \
                            ListPostCategoryAPIView, \
                            DetailPostAPIView, CreatePostAPIView, \
                            RetrieveCategoryAPIView, \
                            RetrieveSubCategoryAPIView, UserCreateAPIView, \
                            ListOfAPIViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^accounts/login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout_then_login, name='logout'),
    url(r'^signup/', UserCreateView.as_view(), name='signup'),
    url(r'^media/(?P<path>.*)', "django.views.static.serve",
        {"document_root": settings.MEDIA_ROOT}),
    url(r'^category/(?P<pk>\d+)', CategoryDetailView.as_view(),
        name="category_detail"
        ),
    url(r'^subcategory/(?P<pk>\d+)/(?P<ordering>\d)',
        SubCategoryItemView.as_view(), name='sub_item_list'),
    url(r'^item_detail/(?P<pk>\d+)', ItemDetailView.as_view(),
        name='item_detail'),
    url(r'^create_listing/(?P<pk>\d+)', MakeListingView.as_view(),
        name='create_listing'),
    url(r'^listapi/$', ListOfAPIViews.as_view(), name='list_of_apis'),
    # Begin API views
    url(r'^api/categories/', ListCategoryAPIView.as_view(), name='category_api_view'),
    url(r'^api/subcategories/', ListSubCategoryAPIView.as_view(), name='subcategory_api_view'),
    url(r'^api/subcategory/(?P<pk>\d+)/posts/', ListPostSubCategoryAPIView.as_view(), name='post_by_subcategory_api_view'),
    url(r'^api/category/(?P<pk>\d+)/posts/', ListPostCategoryAPIView.as_view(), name='post_by_category_api_view'),
    url(r'^api/post/(?P<pk>\d+)', DetailPostAPIView.as_view(), name='post_api_view'),
    url(r'^api/post/create/', CreatePostAPIView.as_view(), name='post_api_view'),
    url(r'^api/category/(?P<pk>\d+)/details/', RetrieveCategoryAPIView.as_view(), name='retrieve_category_api_view'),
    url(r'^api/subcategory/(?P<pk>\d+)/details/', RetrieveSubCategoryAPIView.as_view(), name='retrieve_subcategory_api_view'),
    url(r'^api/user/', UserCreateAPIView.as_view(), name='user_create_view')


    ]
