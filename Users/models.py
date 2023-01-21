from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.Users_Mixins import ModelRequiredProperties
# Create your models here.
from Core.fields import ProjectFields

class User(ModelRequiredProperties.UserMixin,AbstractUser, PermissionsMixin):
    """
    User model for the system with phone number as the unique identifier and whether it is a costumer or market or both
    """
    id = ProjectFields.Id(class_name = "User")
    phone_number = ProjectFields.PhoneNumber(class_name = "User")

    is_customer = ProjectFields.IsCustomer(class_name = "User")
    customer = ProjectFields.CustomerForeignKey(class_name = "User")
    is_market = ProjectFields.IsMarket(class_name = "User")
    market = ProjectFields.MarketForeignKey(class_name = "User")
    is_staff = ProjectFields.IsStaff(class_name = "User")

    is_active = ProjectFields.IsActive(class_name = "User")

    is_admin = ProjectFields.IsAdmin(class_name = "User")

    is_superuser = ProjectFields.IsSuperUser(class_name = "User")
    is_verified = ProjectFields.IsVerified(class_name = "User")

    slug = ProjectFields.Slug(class_name = "User")

    is_delete = ProjectFields.IsDelete(class_name = "User")
    created_at = ProjectFields.CreatedAt(class_name = "User")
    modified_at = ProjectFields.ModifiedAt(class_name = "User")

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
