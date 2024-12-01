from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Task
from .serializers import TaskSerializer

# Create your tests here.

TASKS_URL = reverse('task-list')


def detail_url(task_id):
    return reverse('task-detail', args=[task_id])


def create_task(**params): 
    default = {
        'name' : "Default Task name",
        'text' : "Sample text",
        'priority' : 0,
        'status' : 0,
    }
    default.update(**params)
    task = Task.objects.create(**default)
    return task


def create_user(**params):
    return get_user_model().objects.create(**params)


class PublicMainApiTests(APITestCase):
    """Test unauthorized API requests for main views"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test for unauthorized APIs main"""
        res = self.client.get(TASKS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateMainApiTests(APITestCase):
    """Test authenticated API requests for main views"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com', password='test123')
        self.client.force_authenticate(self.user)

    def test_retrieve_tasks(self):
        create_task(name='Sample first', priority=0, status=1)
        create_task(name='Sample second', priority=1, status=2)
        res = self.client.get(TASKS_URL)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_task(self):
        payload = {
            'name' : "Sample name create",
            'text' : "sample text",
            'priority' : 1,
            'status' : 0,
        }
        res = self.client.post(TASKS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_retrieve_single_task(self):
        task = create_task(name='Sample Task', priority=0, status=0)
        res = self.client.get(detail_url(task.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_partial_task_update(self):
        task = create_task(name='sample task', priority=1, status=0)
        # print(task.finished)
        payload = {
            'status' : 1
        }
        res = self.client.patch(detail_url(task.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(res.data['finished'])

    def test_delete_single_task(self):
        task = create_task()
        res = self.client.delete(detail_url(task.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_full_task_update(self):
        task = create_task()
        payload = {
            'name' : 'updated name',
            'text' : 'updated text',
            'priority' : 2,
            'status' : 1
        }
        res = self.client.put(detail_url(task.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(res.data['finished'])

    def test_filter_status_retrieve(self):
        create_task(name='First task', status=0, priority=0)
        create_task(name='Second task', status=1, priority=0)
        create_task(name='Third task', status=2, priority=0)
        create_task(name='Fourth task', status=1, priority=0)

        res = self.client.get(TASKS_URL, {'status': 1})
        self.assertEqual(len(res.data), 2)

    def test_filter_priority_retrieve(self):
        create_task(name='First task', status=0, priority=1)
        create_task(name='Second task', status=0, priority=2)
        create_task(name='Third task', status=0, priority=1)
        create_task(name='Fourth task', status=0, priority=0)

        res = self.client.get(TASKS_URL, {'priority': 1})
        self.assertEqual(len(res.data), 2)
