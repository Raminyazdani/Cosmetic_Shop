from Core.management.commands.ManagerUtils.CheckLines import check_lines
from Core.management.commands.ManagerUtils.RemoveEmptyLines import remove_empty_lines

def ModelForeigns_maker(File, Models, App_name, Scope_parent, Option):
    header = f"""
from django.utils.functional import cached_property

from Core.utils.ProjectUtils import GetNameSpaceProperty

"""
    result = []
    remove_empty_lines(File)

    if Option == "hard":
        mode_file = "w"
    else:
        mode_file = "a"
        Models = check_lines(File, Models, App_name, Scope_parent, header, prefix= "")

    with open(File, mode_file) as f:
        if mode_file== "w" :
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

        return GetNameSpaceProperty.count(self, teststring,scopeparent)

    @cached_property
    def {Model.lower()}_name(self,teststring="{Model.lower()}",scopeparent="{Scope_parent.lower()}"):
        return GetNameSpaceProperty.name(self, teststring,scopeparent)


"""

            f.write(body)
            result.append(f"{App_name:10}.{Model.capitalize():<25}\t {'ModelForeigns':25} \t\tadded in ModelForeigns.py")
    return result
