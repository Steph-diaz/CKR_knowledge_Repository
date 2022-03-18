from django.shortcuts import render
from rest_framework import viewsets

from api.models import Entry
from api.serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entry.objects.all().order_by('id')
    serializer_class = EntrySerializer
