from django.db import models
from django.utils import timezone
from django.urls import reverse
from pathlib import Path
from ckr_knowledge_repository.users.models import User
from simple_history.models import HistoricalRecords


class Entry(models.Model):
    name = 'entry'

    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    key_words = models.CharField(max_length=60, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    history = HistoricalRecords()

    class Meta:
        app_label = "api"
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        return f"{self.id}: {self.title}"

    # How to find the url of any entry
    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'pk': self.pk})
