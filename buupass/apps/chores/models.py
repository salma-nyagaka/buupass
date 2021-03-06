from django.db import models
from datetime import datetime
from buupass import settings
from buupass.helpers.fancy_generator import fancy_id_generator


class Chores(models.Model):
    id = models.CharField(db_index=True,
                        max_length=256,
                        default=fancy_id_generator,
                        primary_key=True,
                        editable=False)
    title = models.CharField(max_length=30)
    summary = models.TextField(max_length=300)
    completed = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now=True, editable=True)
