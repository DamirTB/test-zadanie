from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime


class Base(models.Model):
    order = models.IntegerField(_('Sorting'), default=0)
    created = models.DateTimeField(auto_now_add=True, 
                                   verbose_name=_('Created'), 
                                   null=True, 
                                   blank=False)
    updated = models.DateTimeField(verbose_name=_('Updated'), 
                                   auto_now=True, 
                                   null=True, 
                                   blank=False)
    is_active = models.BooleanField(_('Public'), default=True)
    is_deleted = models.BooleanField(_('Delete status'), default=False)

    class Meta(object):
        abstract = True

    def save(self, *args, **kwargs):
        self.updated = datetime.datetime.now()
        if not self.created:
            self.created = datetime.datetime.now()
        super(Base, self).save(*args, **kwargs)
