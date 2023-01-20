from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.APP_NAME_Mixins import ModelRequiredProperties
# Create your models here.
from Core.fields import ProjectFields

# Core import
# Create your models here.

# MODEL_NAME
# APP_NAME

from Core.fields import ProjectFields
from Core.models import CoreModelUniversal

class MODEL_NAME(ModelRequiredProperties.MODEL_NAMEMixin,CoreModelUniversal ):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.Name(class_name = "MODEL_NAME")

    # required options

    class Meta:
        verbose_name = _('MODEL_NAME')
        verbose_name_plural = _('MODEL_NAMEs')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

