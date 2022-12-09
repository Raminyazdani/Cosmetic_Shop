from django.db import models

# Create your models here.
class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class Addresses(CoreModel):
    pass


class ProfileBase(CoreModel):
    pass

class Gallery(CoreModel):
    pass

class Images(CoreModel):
    pass

class OrderBase(CoreModel):
    pass