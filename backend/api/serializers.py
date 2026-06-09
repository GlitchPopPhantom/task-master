from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'user']
        # CRITICAL: This MUST be indented inside "class Meta"
        read_only_fields = ['user']
