from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)  # Task description/title
    is_completed = models.BooleanField(default=False)  # Task status

    def __str__(self):
        return self.title
