def models_maker(File, Models, App_name, Scope_parent, Option):
    result = []
    header = f"""
from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.{App_name.capitalize()}_Mixins import Model.capitalize()RequiredProperties
# Create your models here.
from Core.fields import ProjectFields

from Core.fields import ProjectFields
from Core.models import CoreModel.capitalize()Universal
# Core import
# Create your models here.

"""

    with open(File, "w") as f:
        f.write(header)
        for Model in Models:
            body = f"""

class {Model.capitalize()}(Model.capitalize()RequiredProperties.{Model.capitalize()}Mixin,CoreModel.capitalize()Universal ):
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
            result.append(f"{App_name:10}.{Model.capitalize():>25}\t {'Model':25} \t\tadded in models.py")
    return result
