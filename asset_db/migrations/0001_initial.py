# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_id', models.CharField(default='null', max_length=256)),
                ('series_title', models.CharField(default='null', max_length=256)),
                ('season_title', models.CharField(default='null', max_length=256)),
                ('season_number', models.IntegerField(default=0)),
                ('episode_title', models.CharField(default='null', max_length=256)),
                ('episode_number', models.IntegerField(default=0)),
                ('synopsis', models.TextField(default='null', max_length=1024)),
                ('ratings', models.CharField(default='null', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ConformProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=256)),
                ('conform_profile', models.TextField(default='null', max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='FileRepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='null', max_length=256)),
                ('definition', models.CharField(default='null', max_length=256)),
                ('aspect_ratio', models.CharField(default='null', max_length=256)),
                ('seg_1_in', models.CharField(default='null', max_length=12)),
                ('seg_1_dur', models.CharField(default='null', max_length=12)),
                ('seg_2_in', models.CharField(default='null', max_length=12)),
                ('seg_2_dur', models.CharField(default='null', max_length=12)),
                ('seg_3_in', models.CharField(default='null', max_length=12)),
                ('seg_3_dur', models.CharField(default='null', max_length=12)),
                ('seg_4_in', models.CharField(default='null', max_length=12)),
                ('seg_4_dur', models.CharField(default='null', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=256)),
                ('target_path', models.CharField(default='null', max_length=256)),
                ('target_profile', models.TextField(default='null', max_length=1024)),
                ('package_type', models.CharField(default='null', max_length=256)),
                ('video_naming_convention', models.CharField(default='null', max_length=256)),
                ('image_naming_convention', models.CharField(default='null', max_length=256)),
                ('package_naming_convention', models.CharField(default='null', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_id', models.CharField(default='null', max_length=256)),
                ('status', models.CharField(default='null', max_length=256)),
                ('workflow', models.CharField(default='null', max_length=256)),
                ('job_start_time', models.CharField(default='null', max_length=256)),
                ('job_end_time', models.CharField(default='null', max_length=256)),
                ('user', models.CharField(default='null', max_length=256)),
            ],
        ),
    ]
