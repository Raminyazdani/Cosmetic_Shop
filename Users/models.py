from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from Core.models import CoreModel, CoreModelUniversal
from .managers import CostumeBaseUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
    User model for the system with phone number as the unique identifier and whether it is a costumer or market or both
    """
    id = models.BigAutoField(primary_key=True, verbose_name=_('ID'), help_text=_('this is your primary id'),
                             editable=False)
    phone_number = models.CharField(max_length=15, unique=True, validators=[
        RegexValidator(message="must be a phone number", regex='^(\+98|\+980|0098|00980|0)\d{10}$')],
                                    verbose_name=_('Phone Number'),
                                    help_text=_('enter a valid and unique phone number'), db_index=True)

    is_costumer = models.BooleanField(default=False, verbose_name=_('Is Costumer'),
                                      help_text=_('Do you want to have a Costumer Profile?'))
    # costumer_profile_id = models.ForeignKey('CostumerProfile', on_delete=models.SET_NULL, null=True, blank=True,
    #                                         verbose_name=_('Costumer Profile ID'), help_text=_('Costumer Profile ID'),
    #                                         db_index=True)
    is_market = models.BooleanField(default=False, verbose_name=_('Is Market'),
                                    help_text=_('Do you want to have a Market Profile?'))
    # market_profile_id = models.ForeignKey('MarketProfile', on_delete=models.SET_NULL, null=True, blank=True,
    #                                       verbose_name=_('Market Profile ID'), help_text=_('Market Profile ID'),
    #                                       db_index=True)
    is_staff = models.BooleanField(default=False, verbose_name=_('Is Staff'),
                                   help_text=_('Do you want to have a Staff Permissions?'))

    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'), help_text=_('Is this user active?'))

    is_admin = models.BooleanField(default=False, verbose_name=_('Is Admin'),
                                   help_text=_('Do you want to have a Admin Permissions?'))
    is_superuser = models.BooleanField(default=False, verbose_name=_('Is Superuser'),
                                       help_text=_('Do you want to have a Superuser Permissions?'))
    is_verified = models.BooleanField(default=False, verbose_name=_('Is Verified'),
                                      help_text=_('Is this user verified?'))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_('Slug'), help_text=_('Slug Field'),
                            editable=True, default=None, null=True, blank=True)

    is_delete = models.BooleanField(default=False, verbose_name=_('Is Delete'), help_text=_('Is this user deleted?'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'), help_text=_('Created At'))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_('Modified At'), help_text=_('Modified At'))

    objects = CostumeBaseUserManager()
    subset = CostumeBaseUserManager()

    class Admin:
        manager = CostumeBaseUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return reverse('User_detail', args=[str(self.slug)])
        pass

    class meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
