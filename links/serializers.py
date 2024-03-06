from django.urls import reverse
from django.conf import settings
from rest_framework import serializers

from .models import Link
from .go import go


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('link', 'shortcut', 'target', 'time_created',)
        read_only_fields = ('shortcut', 'time_created',)

    link = serializers.SerializerMethodField('get_link')
    target = serializers.URLField()

    def get_link(self, obj: Link):
        return settings.BASE_URL + reverse(go, args=[obj.shortcut])[1:]
