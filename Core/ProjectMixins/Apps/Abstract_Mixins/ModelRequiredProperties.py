from Core.ProjectMixins import Base
from Core.models import CoreModel
from . import ModelForeigns, ModelProperty

# MODEL_NAME
# MODELNAMEEXTRA

class MODEL_NAMEMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.MODEL_NAME
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.MODEL_NAME
