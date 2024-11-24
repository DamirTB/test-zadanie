from django.db import models
from common.models import Base
from .constants import PriorityType, StatusType

# Create your models here.


class Task(Base):
    name = models.CharField(max_length=255, 
                            null=False, 
                            blank=False)
    text = models.TextField(null=True, blank=True)
    priority = models.IntegerField(choices=PriorityType.choices, 
                                   default=PriorityType.LOW)
    status = models.IntegerField(choices=StatusType.choices, 
                                 default=StatusType.IN_PROCESS)
    finished = models.DateTimeField(null=True)    

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
