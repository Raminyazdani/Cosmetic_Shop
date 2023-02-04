from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from Core.ProjectMixins import Base
from . import ModelProperty



class UserMixin(
        # Base Model
        AbstractBaseUser, PermissionsMixin,
        # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # str and absolute url methods
        # PROPERTIES

        # MANAGERS
        ):
    #todo do this

    """
    Users.User Model Mixin
    """
    class Meta:
        abstract = True
    objects = ModelProperty.Manager.OBJECTS.USER
    subsets = ModelProperty.Manager.SUBSETS.USER
    USERNAME_FIELD = ModelProperty.USERNAME.USER
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.USER
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.USER
