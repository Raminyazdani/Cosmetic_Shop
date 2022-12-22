from django.db import models

# Create your models here.

class CoreModel(models.Model):

    class Meta:
        abstract = True

class CoreModelUniversal(CoreModel):
    time_created = models.DateTimeField
    time_modified = models.DateTimeField
    is_delete = models.BooleanField
    is_active = models.BooleanField
    class Meta:
        abstract=True
