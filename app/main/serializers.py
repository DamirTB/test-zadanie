from rest_framework import serializers
from .models import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Tasks"""

    class Meta:
        model = Task
        fields = ['id', 'name', 'text', 'priority', 'status', 
                  'finished', 'created']


class TaskDetailSerializer(TaskSerializer):
    """Detailed Serializer for Tasks"""

    class Meta(TaskSerializer.Meta):
        extra_kwargs = {
            'created' : {'read_only' : True},
            'name' : {'read_only' : True}
        }

    def update(self, instance, validated_data):
        if validated_data['status'] == 1 and \
           instance.status != validated_data['status']:
            validated_data['finished'] = timezone.now()
        return super().update(instance, validated_data)
