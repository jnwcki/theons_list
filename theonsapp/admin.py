from django.contrib import admin
from theonsapp.models import UserProfile, Item, City, Category, SubCategory

admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(SubCategory)