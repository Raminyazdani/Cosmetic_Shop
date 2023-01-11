def ModelRequiredProperties_maker(File, Models, App_name, Scope_parent, Option):
    result = []
    header = f"""
from Core.ProjectMixins import Base
from Core.models import CoreModel
from . import ModelForeigns, ModelProperty
"""

    with open(File, "w") as f:
        f.write(header)
        for Model in Models:
            body = f"""

class {Model.capitalize()}Mixin(  # METHODS
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

    \"\"\"
    {App_name.capitalize()}.{Model.capitalize()} Mixin
    \"\"\"
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.{Model.upper()}
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.{Model.upper()}
"""
            f.write(body)
            result.append(f"{App_name:10}.{Model.capitalize():>25}\t {'ModelRequiredProperties':25} \t\tadded in ModelRequiredProperties.py")
    return result
