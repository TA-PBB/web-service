from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.TextField(max_length=20, unique=True)
    password = models.TextField(max_length=8)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
    
class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TaskItem(models.Model):
    task = models.ForeignKey(Task, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description