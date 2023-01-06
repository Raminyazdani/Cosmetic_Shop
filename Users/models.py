from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from Core.models import CoreModel, CoreModelUniversal
from Core.fields import ProjectField
from Core.ProjectMixins.Users import Property, ModelRequiredProperties
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin,ModelRequiredProperties.User):
    """
    User model for the system with phone number as the unique identifier and whether it is a costumer or market or both
    """
    id = ProjectField.CustomIdField(class_name="User")
    phone_number = ProjectField.CustomPhoneNumberField(class_name="User")

    is_costumer = ProjectField.CustomIsCostumerField(class_name="User")
    # costumer_profile_id = models.ForeignKey('CostumerProfile', on_delete=models.SET_NULL, null=True, blank=True,
    #                                         verbose_name=_('Costumer Profile ID'), help_text=_('Costumer Profile ID'),
    #                                         db_index=True)
    is_market = ProjectField.CustomIsMarketField(class_name="User")
    # market_profile_id = models.ForeignKey('MarketProfile', on_delete=models.SET_NULL, null=True, blank=True,
    #                                       verbose_name=_('Market Profile ID'), help_text=_('Market Profile ID'),
    #                                       db_index=True)
    is_staff = ProjectField.CustomIsStaffField(class_name="User")

    is_active = ProjectField.CustomIsActiveField(class_name="User")

    is_admin = ProjectField.CustomIsAdminField(class_name="User")

    is_superuser = ProjectField.CustomIsSuperUserField(class_name="User")
    is_verified = ProjectField.CustomIsVerifiedField(class_name= "User")

    slug = ProjectField.CustomSlugField(class_name="User")

    is_delete = ProjectField.CustomIsDeletedField(class_name="User")
    created_at = ProjectField.CustomCreatedAtField(class_name="User")
    modified_at = ProjectField.CustomModifiedAtField(class_name="User")

    objects= Property.Manager.USER_OBJECT
    subset = Property.Manager.USER_SUBSET

    USERNAME_FIELD = Property.UserNameField.USER
    REQUIRED_FIELDS = Property.RequiredField.USER
    SEARCH_FIELDS = Property.SearchFields.USER

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
