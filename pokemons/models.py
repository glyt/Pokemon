from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=140)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
