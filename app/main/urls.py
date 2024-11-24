from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
