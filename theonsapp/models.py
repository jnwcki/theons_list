from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    home_city = models.ForeignKey(City, null=True)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    location = models.ForeignKey(City)
    seller = models.ForeignKey("auth.User", related_name="item_for_sale")
    name = models.CharField(max_length=100)
    full_description = models.TextField()
    time_listed = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='uploads', default='uploads/default.png')
    price = models.IntegerField()
    subcategory = models.ForeignKey(SubCategory)

    def __str__(self):
        return self.name


@receiver(post_save, sender="auth.User")
def user_profile_create(sender, **kwargs):
    created = kwargs.get("created")
    if created:
        instance = kwargs.get("instance")
        UserProfile.objects.create(user=instance)

