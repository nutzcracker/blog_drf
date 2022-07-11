from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Dossier
from rest_framework.response import Response
from rest_framework import permissions

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Dossier.objects.all()
    lookup_field = 'urls'
    permission_classes = [permissions.AllowAny]


