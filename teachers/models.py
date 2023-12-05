from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='teachers/%Y/%m/%d')

    class Meta:
        ordering = ['first_name']

        indexes = [models.Index(fields=['first_name'])]
