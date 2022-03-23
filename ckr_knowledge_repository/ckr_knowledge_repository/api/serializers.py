from api.models import Entry
from rest_framework import serializers


class EntrySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Entry
        fields = '__all__'
