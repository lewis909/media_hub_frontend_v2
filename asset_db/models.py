from django.db import models

# Create your models here.

class AssetMetadata(models.Model):

    id = models.DecimalField(6).auto_creation_counter
    material_id = models.CharField(max_length=256, default='null')
    series_title = models.CharField(max_length=256, default='null')
    season_title = models.CharField(max_length=256, default='null')
    season_number = models.IntegerField(default=0)
    episode_title = models.CharField(max_length=256, default='null')
    episode_number = models.IntegerField(default=0)
    synopsis = models.TextField(max_length=1024, default='null')
    ratings = models.CharField(max_length=256, default='null')


class Profiles(models.Model):

    id = models.DecimalField(6).auto_creation_counter
    name = models.CharField(max_length=256, default='null')
    target_path = models.CharField(max_length=256, default='null')
    target_profile = models.TextField(max_length=1024, default='null')
    package_type = models.CharField(max_length=256, default='null')
    video_naming_convention = models.CharField(max_length=256, default='null')
    image_naming_convention = models.CharField(max_length=256, default='null')
    package_naming_convention = models.CharField(max_length=256, default='null')


class ConformProfiles(models.Model):

    id = models.DecimalField.auto_creation_counter
    name = models.CharField(max_length=256, default='null')
    conform_profile = models.TextField(max_length=1024, default='null')


class Task(models.Model):
    task_id = models.DecimalField(6).auto_creation_counter
    material_id = models.CharField(max_length=256, default='null')
    status = models.CharField(max_length=256, default='null')
    workflow = models.CharField(max_length=256, default='null')
    job_start_time = models.CharField(max_length=256, default='null')
    job_end_time = models.CharField(max_length=256, default='null')
    user = models.CharField(max_length=256, default='null')


class FileRepo(models.Model):
    id = models.DecimalField.auto_creation_counter
    filename = models.CharField(max_length=256, default='null')
    definition = models.CharField(max_length=256, default='null')
    aspect_ratio = models.CharField(max_length=256, default='null')
    number_of_segments = models.DecimalField.auto_creation_counter
    seg_1_in = models.CharField(max_length=12, default='null')
    seg_1_dur = models.CharField(max_length=12, default='null')
    seg_2_in = models.CharField(max_length=12, default='null')
    seg_2_dur = models.CharField(max_length=12, default='null')
    seg_3_in = models.CharField(max_length=12, default='null')
    seg_3_dur = models.CharField(max_length=12, default='null')
    seg_4_in = models.CharField(max_length=12, default='null')
    seg_4_dur = models.CharField(max_length=12, default='null')
