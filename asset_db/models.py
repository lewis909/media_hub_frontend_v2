from django.db import models


class AssetMetadata(models.Model):

    id = models.DecimalField(6).auto_creation_counter
    material_id = models.CharField(max_length=256, blank=True)
    series_title = models.CharField(max_length=256, blank=True)
    season_title = models.CharField(max_length=256, blank=True)
    season_number = models.IntegerField(default=0)
    episode_title = models.CharField(max_length=256, blank=True)
    episode_number = models.IntegerField(default=0)
    synopsis = models.TextField(max_length=1024, blank=True)
    ratings = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.material_id


class Profiles(models.Model):

    id = models.DecimalField(6).auto_creation_counter
    name = models.CharField(max_length=256, blank=True)
    target_path = models.CharField(max_length=256, blank=True)
    target_profile = models.TextField(max_length=1024, blank=True)
    package_type = models.CharField(max_length=256, blank=True)
    video_naming_convention = models.CharField(max_length=256, blank=True)
    image_naming_convention = models.CharField(max_length=256, blank=True)
    package_naming_convention = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class ConformProfiles(models.Model):

    name = models.CharField(max_length=256, blank=True)
    conform_profile = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):

    material_id = models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, blank=True)
    workflow = models.CharField(max_length=256, blank=True)
    job_start_time = models.CharField(max_length=256, blank=True)
    job_end_time = models.CharField(max_length=256, blank=True)
    user = models.CharField(max_length=256, blank=True)


    def __str__(self):
        return str(self.id)


class FileRepo(models.Model):
    id = models.DecimalField.auto_creation_counter
    filename = models.CharField(max_length=256, blank=True)
    definition = models.CharField(max_length=256, blank=True)
    aspect_ratio = models.CharField(max_length=256, blank=True)
    number_of_segments = models.CharField(max_length=2, blank=True)
    seg_1_in = models.CharField(max_length=12, blank=True)
    seg_1_dur = models.CharField(max_length=12, blank=True)
    seg_2_in = models.CharField(max_length=12, blank=True)
    seg_2_dur = models.CharField(max_length=12, blank=True)
    seg_3_in = models.CharField(max_length=12, blank=True)
    seg_3_dur = models.CharField(max_length=12, blank=True)
    seg_4_in = models.CharField(max_length=12, blank=True)
    seg_4_dur = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.filename
