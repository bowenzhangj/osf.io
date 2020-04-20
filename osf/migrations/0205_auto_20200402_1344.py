# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-04-02 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import osf.models.base


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0204_ensure_schemas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('hero_logo_image', models.URLField()),
                ('topnav_logo_image', models.URLField()),
                ('hero_background_image', models.URLField()),
                ('primary_color', models.CharField(max_length=7)),
                ('secondary_color', models.CharField(max_length=7)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, osf.models.base.QuerySetExplainMixin),
        ),
        migrations.AddField(
            model_name='abstractprovider',
            name='advertises_on_discovery',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='abstractprovider',
            name='branded_discovery_page',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='abstractprovider',
            name='has_landing_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='abstractprovider',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='providers', to='osf.Brand'),
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'permissions': (('view_brand', 'Can view brand details'), ('modify_brand', 'Can modify brands'))},
        ),
    ]
