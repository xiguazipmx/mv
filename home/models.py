# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MvAvatar(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255, blank=True, null=True)
    alt = models.CharField(max_length=255, blank=True, null=True)
    image_small = models.CharField(max_length=255, blank=True, null=True)
    image_medium = models.CharField(max_length=255, blank=True, null=True)
    image_large = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mv_avatar'


class MvDirector(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255, blank=True, null=True)
    alt = models.CharField(max_length=255, blank=True, null=True)
    image_small = models.CharField(max_length=255, blank=True, null=True)
    image_medium = models.CharField(max_length=255, blank=True, null=True)
    image_large = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mv_director'


class MvGenres(models.Model):
    id = models.CharField(max_length=50)
    genres = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'mv_genres'


class MvMovie(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    subtype = models.CharField(max_length=255)
    directors = models.CharField(max_length=50)
    genres = models.CharField(max_length=255, blank=True, null=True)
    average = models.CharField(max_length=50, blank=True, null=True)
    max = models.CharField(max_length=50, blank=True, null=True)
    min = models.CharField(max_length=50, blank=True, null=True)
    stars = models.CharField(max_length=50, blank=True, null=True)
    collect_count = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mv_movie'


class MvMovieAvatarIds(models.Model):
    movie_id = models.CharField(max_length=50, blank=True, null=True)
    avatar_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mv_movie_avatar_ids'
