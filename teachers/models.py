from django.db import models
from django.urls import reverse

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='teachers/%Y/%m/%d')

    def get_absolute_url(self):
        return reverse('teachers:teacher_detail', args=[self.slug])
    

    class Meta:
        ordering = ['first_name']

        indexes = [models.Index(fields=['first_name'])]
