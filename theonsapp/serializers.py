from django.contrib.auth.models import User
from rest_framework import serializers
from theonsapp.models import Category, SubCategory, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
