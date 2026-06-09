from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'user']
        # This completely stops the frontend from being forced to send a user ID
        read_only_fields = ['user']
