from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
from Core.managers import BaseManager


class CoreModel(models.Model):
    class Meta:
        abstract = True



class CoreModelUniversal(CoreModel):

    is_delete = models.BooleanField(default=False, verbose_name=_('Is Delete'), help_text=_('Is this user deleted?'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'), help_text=_('Created At'))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_('Modified At'), help_text=_('Modified At'))

    class Meta:
        abstract = True


