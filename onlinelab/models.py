# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import ArrayField
from any_imagefield.models import AnyImageField


class Project(models.Model):

    TYPE_STORE = "store"
    TYPE_RESOURCE = "resource"
    TYPE_PORTAL = "portal"
    TYPE_MOBILE_APP = "mobile_app"
    TYPE_MARKETING = "marketing"
    TYPE_ELECTRONICS = "electronics"

    TYPE_CHOICES = (
        (TYPE_STORE, "Интернет-магазин"),
        (TYPE_RESOURCE, "Ресурс"),
        (TYPE_PORTAL, "Корпоративный портал"),
        (TYPE_MOBILE_APP, "Мобильное приложение"),
        (TYPE_MARKETING, "Маркетинг"),
        (TYPE_ELECTRONICS, "Электроника"),
    )

    name = models.CharField("Название", max_length=100, null=True, blank=True)
    description_short = models.TextField("Краткое описание", null=True, blank=True)
    kind = models.CharField("Тип", max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    logo_image = AnyImageField(verbose_name="Логитип проекта", help_text='Для главной', null=True, blank=True)
    card_image = AnyImageField(verbose_name="Карточка проекта", help_text='Большая', null=True, blank=True)
    header_image = AnyImageField(verbose_name="Картика в шапку", null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)
    side_column = models.TextField("Боковая колонка", null=True, blank=True)
    our_project_image = AnyImageField(
        verbose_name="Карточка нашего проекта", help_text='Если наш проект', null=True, blank=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __unicode__(self):
        return "Проект %s" % self.name


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=250, null=True, blank=True)
    text = models.TextField("Текст", null=True, blank=True)
    tags = ArrayField(models.CharField(max_length=200), verbose_name="Теги", blank=True)
    author = models.CharField("Автор", max_length=50, null=True, blank=True)
    date = models.DateField("Дата", default=timezone.now)
    header_image = AnyImageField(verbose_name="Картинка-шапка", null=True, blank=True)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __unicode__(self):
        return "Запись %s" % self.title

    def save(self, *args, **kwargs):
        self.tags = map(unicode.strip, self.tags)
        super(Post, self).save(*args, **kwargs)
