from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):
    city_name = models.CharField(max_length=50)


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    home_city = models.ForeignKey(City, null=True)


class Item(models.Model):
    location = models.ForeignKey(City)
    seller = models.ForeignKey("auth.User", related_name="item_for_sale")
    name = models.CharField(max_length=100)
    full_description = models.TextField()
    time_listed = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()


@receiver(post_save, sender="auth.User")
def user_profile_create(sender, **kwargs):
    created = kwargs.get("created")
    if created:
        instance = kwargs.get("instance")
        UserProfile.objects.create(user=instance)


