from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'user']
        # This line is the missing link—it tells DRF that the frontend 
        # doesn't need to send the user ID manually in the POST body
        read_only_fields = ['user']
