from Core.management.commands.ManagerUtils.CheckLines import check_lines
from Core.management.commands.ManagerUtils.RemoveEmptyLines import remove_empty_lines

def models_maker(File, Models, App_name, Scope_parent, Option):
    header = f"""
from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.{App_name.capitalize()}_Mixins import ModelRequiredProperties
from Core.fields import ProjectFields

from Core.fields import ProjectFields
from Core.models import CoreModelUniversal


"""
    result = []
    remove_empty_lines(File)

    if Option == "hard":
        mode_file = "w"
    else:
        mode_file = "a"
        Models = check_lines(File, Models, App_name, Scope_parent, header, prefix = "")

    with open(File, mode_file) as f:
        if mode_file == "w":
            f.write(header)
        for Model in Models:
            body = f"""
class {Model.capitalize()}(ModelRequiredProperties.{Model.capitalize()}Mixin,CoreModelUniversal ):
    \"\"\"
    Product Model.capitalize()
    \"\"\"
    # \"\"\" Fields   \"\"\"
    name = ProjectFields.CustomNameField(class_name = "{Model.capitalize()}")

    # required options

    class Meta:
        verbose_name = _('{Model.capitalize()}')
        verbose_name_plural = _('{Model.capitalize()}s')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

"""

            f.write(body)
            result.append(f"{App_name:10}.{Model.capitalize():<25}\t {'Model':25} \t\tadded in models.py")
    return result
