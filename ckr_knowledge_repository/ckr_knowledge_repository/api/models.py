from django.db import models
from pathlib import Path


class Entry(models.Model):
    name = 'entry'
    entry_id = models.IntegerField(null=False, blank=False, unique=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    keywords = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        app_label = "api"
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        return f"{self.entry_id}: {self.title}"
