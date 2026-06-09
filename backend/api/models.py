from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Link every task to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
