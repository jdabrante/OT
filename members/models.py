from django.db import models
from music.models import MusicStyle

class Competitor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    birthdate = models.DateTimeField()
    subject = models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    hobbies = models.TextField()
    music_style = models.ForeignKey(MusicStyle, on_delete=models.CASCADE, related_name='competitors')
    avatar = models.ImageField(upload_to='competitor/%Y/%m/%d')

    class Meta: 
        ordering = ['first_name']

        indexes = [
            models.Index(fields=['first_name'])
        ]
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    avatar = models.ImageField(upload_to='teacher/%Y/%m/%d')

    class Meta: 
        ordering = ['first_name']

        indexes = [
            models.Index(fields=['first_name'])
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Judge(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    job = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='judge/%Y/%m/%d')