from rest_framework import serializers
from .models import Dossier
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth.models import User


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):

    tag = TagListSerializerField()
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Dossier
        fields = ("id", "name", "urls", "description", "photo", "tag", "author")
        lookup_field = 'urls'
        extra_kwargs = {
            'url': {'lookup_field': 'urls'}
        }