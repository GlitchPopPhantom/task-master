from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # This completely forces Django to ignore the user field when creating a task
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'user']
