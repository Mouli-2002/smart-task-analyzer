from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
import json

class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    estimated_hours = models.IntegerField(default=1)
    importance = models.IntegerField(default=5)   # scale 1–10
    dependencies = models.JSONField(default=list) # store list of task IDs or names

    def __str__(self):
        return self.title
