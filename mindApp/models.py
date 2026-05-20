from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders")
    message = models.TextField()  # e.g. "Buy milk"
    remind_at = models.DateTimeField()  # when to trigger
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.message} at {self.remind_at}"
