# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.contrib import admin
from django.db import models
from redactor.widgets import RedactorEditor
from .models import Post, Project


class EditorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': RedactorEditor}
    }


admin.site.register(Post, EditorAdmin)
admin.site.register(Project, EditorAdmin)
