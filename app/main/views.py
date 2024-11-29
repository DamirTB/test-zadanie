from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone 

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Tasks
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['priority', 'status']

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     new_status = request.data.get('status')
    #     if new_status == 1 and instance.status != 1:
    #         instance.finished = timezone.now()
    #     instance.status = new_status

    #     serializer = TaskSerializer(data=request.data)
        
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

    # def get_serializer_class(self):
    #     if self.action == 'update' or self.action == 'partial_update':
    #         return TaskSerializer
    #     return TaskDetailSerializer
