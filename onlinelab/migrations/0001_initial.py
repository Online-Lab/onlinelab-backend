# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None, verbose_name='\u0422\u0435\u0433\u0438', blank=True)),
                ('author', models.CharField(max_length=50, verbose_name='\u0410\u0432\u0442\u043e\u0440')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043f\u0438\u0441\u044c',
                'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description_short', models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('kind', models.CharField(max_length=20, verbose_name='\u0422\u0438\u043f', choices=[('store', '\u0418\u043d\u0442\u0435\u0440\u043d\u0435\u0442-\u043c\u0430\u0433\u0430\u0437\u0438\u043d'), ('resource', '\u0420\u0435\u0441\u0443\u0440\u0441'), ('portal', '\u041a\u043e\u0440\u043f\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0439 \u043f\u043e\u0440\u0442\u0430\u043b'), ('mobile_app', '\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435'), ('marketing', '\u041c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433'), ('electronics', '\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0430')])),
                ('logo_image', models.ImageField(help_text='\u0414\u043b\u044f \u0433\u043b\u0430\u0432\u043d\u043e\u0439', upload_to=b'', verbose_name='\u041b\u043e\u0433\u0438\u0442\u0438\u043f \u043f\u0440\u043e\u0435\u043a\u0442\u0430')),
                ('card_image', models.ImageField(help_text='\u0411\u043e\u043b\u044c\u0448\u0430\u044f', upload_to=b'', verbose_name='\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430')),
                ('header_image', models.ImageField(upload_to=b'', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043a\u0430 \u0432 \u0448\u0430\u043f\u043a\u0443')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('side_column', models.TextField(verbose_name='\u0411\u043e\u043a\u043e\u0432\u0430\u044f \u043a\u043e\u043b\u043e\u043d\u043a\u0430')),
                ('our_project_image', models.ImageField(help_text='\u0415\u0441\u043b\u0438 \u043d\u0430\u0448 \u043f\u0440\u043e\u0435\u043a\u0442', upload_to=b'', null=True, verbose_name='\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043d\u0430\u0448\u0435\u0433\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0435\u043a\u0442\u044b',
            },
        ),
    ]
