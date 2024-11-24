from django.db import models
from django.utils.translation import gettext_lazy as _


class PriorityType(models.IntegerChoices):
    LOW = 0, _("LOW")
    MEDIUM = 1, _("MEDIUM")
    HIGH = 2, _("HIGH")


class StatusType(models.IntegerChoices):
    IN_PROCESS = 0, _("IN_PROCESS")
    COMPLETED = 1, _("COMPLETED")
    CANCELED = 2, _("CANCELED")
