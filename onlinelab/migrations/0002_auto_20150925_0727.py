# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import any_imagefield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('onlinelab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=any_imagefield.models.fields.AnyImageField(default='', upload_to=b'', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430-\u0448\u0430\u043f\u043a\u0430'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='card_image',
            field=any_imagefield.models.fields.AnyImageField(help_text='\u0411\u043e\u043b\u044c\u0448\u0430\u044f', upload_to=b'', verbose_name='\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='project',
            name='header_image',
            field=any_imagefield.models.fields.AnyImageField(upload_to=b'', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043a\u0430 \u0432 \u0448\u0430\u043f\u043a\u0443'),
        ),
        migrations.AlterField(
            model_name='project',
            name='logo_image',
            field=any_imagefield.models.fields.AnyImageField(help_text='\u0414\u043b\u044f \u0433\u043b\u0430\u0432\u043d\u043e\u0439', upload_to=b'', verbose_name='\u041b\u043e\u0433\u0438\u0442\u0438\u043f \u043f\u0440\u043e\u0435\u043a\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='project',
            name='our_project_image',
            field=any_imagefield.models.fields.AnyImageField(help_text='\u0415\u0441\u043b\u0438 \u043d\u0430\u0448 \u043f\u0440\u043e\u0435\u043a\u0442', upload_to=b'', null=True, verbose_name='\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043d\u0430\u0448\u0435\u0433\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430', blank=True),
        ),
    ]
