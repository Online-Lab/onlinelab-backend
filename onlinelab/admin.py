# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.contrib import admin
from .models import Post, Project


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
