from django.db import models


class Event(models.Model):
    photo = models.ImageField(upload_to='photos')
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
