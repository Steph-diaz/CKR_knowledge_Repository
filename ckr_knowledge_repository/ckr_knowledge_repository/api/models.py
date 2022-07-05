from django.db import models
from django.utils import timezone
from django.urls import reverse
from pathlib import Path
from ckr_knowledge_repository.users.models import User
from simple_history.models import HistoricalRecords

STATUS_CHOICES = (
    ('IN_PROGRESS', 'In Progress'),
    ('APPROVED', 'Approved'),
)

ENTRY_RECORD = (
    ('ACTIVE', 'Active'),
    ('ARCHIVED', 'Archived'),
)

TYPES = (
    ('Animal', 'Animals'),
    ('BP', 'Business processes'),
    ('CellAg', 'Cellular agriculture'),
    ('Comms', 'Communications'),
    ('EmgSci', 'Emerging Science'),
    ('Ingr', 'Ingredients or substances'),
    ('Intl', 'International'),
    ('Inqs', 'Inquiries'),
    ('JClub', 'Journal Club'),
    ('Microb', 'Microbes'),
    ('MMEval', 'Molecular and micro review'),
    ('Plants', 'Plants'),
    ('Regs', 'Regulatory'),
    ('PreMkt', 'Pre-market'),
    ('Troubl', 'Technical troubleshooting'),
    ('MMTech', 'Technologies')
)


class Entry(models.Model):
    name = 'entry'

    entry_number = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=50, choices=TYPES, default='Animal')
    content = models.TextField(null=True, blank=True)
    links = models.TextField(null=True, blank=True)
    key_words = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='IN_PROGRESS')
    record = models.CharField(max_length=50, choices=ENTRY_RECORD, default='ACTIVE')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
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
