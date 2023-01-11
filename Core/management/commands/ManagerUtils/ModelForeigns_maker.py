def ModelForeigns_maker(File, Models, App_name, Scope_parent, Option):
    result = []
    header = f"""
from django.utils.functional import cached_property

from Core.utils.ProjectUtils import GetNameSpaceProperty

"""

    with open(File, "w") as f:
        f.write(header)
        for Model in Models:
            body = f"""

class {Model.capitalize()}:
    class Meta:
        abstract = True

    \"\"\"
    {Model.capitalize()} Mixin
    \"\"\"

    @cached_property
    def {Model.lower()}_count(self,teststring="{Model.lower()}",scopeparent="{Scope_parent.lower()}"):

        return GetNameSpaceProperty.count(self, "{Model.lower()}","{Scope_parent.lower()}")

    @cached_property
    def {Model.lower()}_name(self,teststring="{Model.lower()}",scopeparent="{Scope_parent.lower()}"):
        return GetNameSpaceProperty.name(self, "{Model.lower()}","{Scope_parent.lower()}")


"""

            f.write(body)
            result.append(f"{App_name:10}.{Model.capitalize():>25}\t {'ModelForeigns':25} \t\tadded in ModelForeigns.py")
    return result
