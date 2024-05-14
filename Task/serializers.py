from rest_framework import serializers
from .models import Task, TaskItem

class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ['id', 'id_task', 'description']

class TaskSerializer(serializers.ModelSerializer):
    items = TaskItemSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'created_at', 'updated_at', 'items']
