from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return self.title

class TaskItem(models.Model):
    id_task = models.ForeignKey(Task, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=250)