from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Tasks"""

    class Meta:
        model = Task
        fields = ['name', 'text', 'priority', 'status']
        read_only_fields = ['id', 'created', 'finished']
