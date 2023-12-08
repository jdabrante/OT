from django.db import models
from django.urls import reverse


class MusicStyle(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)


class Competitor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    birthdate = models.DateField()
    city = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    hobbies = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='competitors/%Y/%m/%d')
    music_styles = models.ManyToManyField(MusicStyle)

    class Meta:
        ordering = ['first_name']

        indexes = [models.Index(fields=['first_name'])]

    def get_absolute_url(self):
        return reverse('competitors:competitor_detail', args=[self.slug])
