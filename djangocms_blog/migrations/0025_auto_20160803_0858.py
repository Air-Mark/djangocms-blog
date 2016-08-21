# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-03 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0024_auto_20160706_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='djangocms_blog.BlogCategory', verbose_name='parent'),
        ),
    ]
