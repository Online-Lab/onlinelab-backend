# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from rest_framework import viewsets, filters
from .models import Project, Post
from .serializers import ProjectSerializer, PostSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('kind',)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('tags',)
