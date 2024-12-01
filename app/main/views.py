from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Tasks

    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['priority', 'status']

    @swagger_auto_schema(
        operation_summary="List all tasks",
        operation_description="Retrieve a list of tasks, \
        filter by priority or status",
        responses={200: TaskSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return TaskDetailSerializer
        return TaskSerializer
