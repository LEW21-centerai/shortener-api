from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string
import string


class Link(models.Model):
    SHORTCUT_LETTERS = string.ascii_lowercase + string.digits

    @staticmethod
    def make_random_shortcut():
        return get_random_string(getattr(settings, 'SHORTCUT_LENGTH', 4), allowed_chars=Link.SHORTCUT_LETTERS)

    shortcut = models.CharField(max_length=50, primary_key=True, blank=False)
    target = models.URLField(max_length=255, unique=True)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']
