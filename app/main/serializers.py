from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Tasks"""

    class Meta:
        model = Task
        fields = ['id', 'name', 'text', 'priority', 'status', 'finished', 'created']

    def update(self, instance, validated_data):
        if 'status' in validated_data and validated_data['status'] == 1 and instance.status != 1:
            validated_data['finished'] = timezone.now()
        return super().update(instance, validated_data)


class TaskDetailSerializer(TaskSerializer):
    """Serializer for Tasks"""

    class Meta(TaskSerializer.Meta):
        fields = TaskSerializer.Meta.fields + ['created', 'finished']
        extra_kwargs = {
            'created' : {'read_only' : True}
        }
