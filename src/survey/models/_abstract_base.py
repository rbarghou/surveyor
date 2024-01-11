import uuid

from django.db import models


class AbstractBase(models.Model):
    """AbstractBase"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
