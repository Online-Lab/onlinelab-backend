# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import any_imagefield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('onlinelab', '0002_auto_20150925_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=50, null=True, verbose_name='\u0410\u0432\u0442\u043e\u0440', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=any_imagefield.models.fields.AnyImageField(upload_to=b'', null=True, verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430-\u0448\u0430\u043f\u043a\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='card_image',
            field=any_imagefield.models.fields.AnyImageField(help_text='\u0411\u043e\u043b\u044c\u0448\u0430\u044f', upload_to=b'', null=True, verbose_name='\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_short',
            field=models.TextField(null=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='header_image',
            field=any_imagefield.models.fields.AnyImageField(upload_to=b'', null=True, verbose_name='\u041a\u0430\u0440\u0442\u0438\u043a\u0430 \u0432 \u0448\u0430\u043f\u043a\u0443', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='kind',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u0422\u0438\u043f', choices=[('store', '\u0418\u043d\u0442\u0435\u0440\u043d\u0435\u0442-\u043c\u0430\u0433\u0430\u0437\u0438\u043d'), ('resource', '\u0420\u0435\u0441\u0443\u0440\u0441'), ('portal', '\u041a\u043e\u0440\u043f\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0439 \u043f\u043e\u0440\u0442\u0430\u043b'), ('mobile_app', '\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435'), ('marketing', '\u041c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433'), ('electronics', '\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0430')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='logo_image',
            field=any_imagefield.models.fields.AnyImageField(help_text='\u0414\u043b\u044f \u0433\u043b\u0430\u0432\u043d\u043e\u0439', upload_to=b'', null=True, verbose_name='\u041b\u043e\u0433\u0438\u0442\u0438\u043f \u043f\u0440\u043e\u0435\u043a\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='side_column',
            field=models.TextField(null=True, verbose_name='\u0411\u043e\u043a\u043e\u0432\u0430\u044f \u043a\u043e\u043b\u043e\u043d\u043a\u0430', blank=True),
        ),
    ]
