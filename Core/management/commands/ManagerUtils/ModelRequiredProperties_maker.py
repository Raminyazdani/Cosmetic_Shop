from Core.management.commands.ManagerUtils.CheckLines import check_lines
from Core.management.commands.ManagerUtils.RemoveEmptyLines import remove_empty_lines

def ModelRequiredProperties_maker(File, Models, App_name, Scope_parent, Option):
    header = f"""
from Core.ProjectMixins import Base
from Core.models import CoreModel
from . import ModelForeigns, ModelProperty
"""
    result = []
    remove_empty_lines(File)

    if Option == "hard":
        mode_file = "w"
    else:
        mode_file = "a"
        Models = check_lines(File, Models, App_name, Scope_parent, header, prefix = "Mixin")

    with open(File, mode_file) as f:
        if mode_file == "w":
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
            result.append(f"{App_name:10}.{Model.capitalize():<25}\t {'ModelRequiredProperties':25} \t\tadded in ModelRequiredProperties.py")
    return result
