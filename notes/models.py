from django.db import models
from uuid import uuid4


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # TODO: add user/author who created the note
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # TODO: tagging system or categories
