# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-17 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.TextField()),
                ('author_link', models.URLField()),
                ('origin_text', models.TextField()),
                ('origin_link', models.URLField()),
                ('description', models.TextField()),
                ('methods', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='aesthetic_computation.Category')),
            ],
        ),
    ]
