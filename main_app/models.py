from django.db import models
from django.urls import reverse

# Create your models here.

class Wig(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    length = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'wig_id': self.id})