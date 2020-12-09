from django.contrib.auth.models import User
from blogs.models import BlogPost
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id','title', 'body', 'image', 'date_updated','comments']