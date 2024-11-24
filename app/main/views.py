from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Tasks
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['priority', 'status']
