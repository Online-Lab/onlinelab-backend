# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from rest_framework import serializers
from .models import Project, Post


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Project


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Post
