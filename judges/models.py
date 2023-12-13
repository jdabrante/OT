from django.db import models
from django.urls import reverse

class Judge(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    job = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(upload_to='judges/%Y/%m/%d')
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("judges:judge_detail", args=[self.slug])
    

    class Meta:
        ordering = ['first_name']

        indexes = [models.Index(fields=['first_name'])]
