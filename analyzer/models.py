from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    importance = models.IntegerField(null=True, blank=True)  # 1-10 scale
    effort = models.IntegerField(null=True, blank=True)  # estimated hours
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
