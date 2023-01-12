import os
import re
import shutil

from django.core.management.base import BaseCommand
from .ManagerUtils.field_templates import REQUIRED
from Core.management.commands.ManagerUtils import field_templates
from Cosmetic_Shop.settings import BASE_DIR

def readfile(File):
    regex_super_class = re.compile(r"(^[a-zA-Z]+)")
    regex_sub_class = re.compile(r"\s+([a-zA-Z]+)")
    sub_class_list = []
    super_class_list = []
    with open(File, 'r') as f:
        lines = f.readlines()
        super = ""
        for line in lines:
            if regex_sub_class.match(line):
                if super in ["ForeignKeyABC", "GenericForeignKeyABC", "GenericRelationABC"]:
                    sub_class_list.append((super[:-3] + ".py", regex_sub_class.match(line).group(1)))
                else:
                    sub_class_list.append((super[:-3] + "Fields.py", regex_sub_class.match(line).group(1)))
            elif regex_super_class.match(line):
                super_class_list.append(("DefaultFields.py", regex_super_class.match(line).group(1)))
                super = super_class_list[-1][1]

    return super_class_list, sub_class_list

def make_super_class(Dirs, kwargs, path_route, class_name):
    pass

def make_sub_class(Dirs, kwargs, path_route, class_name):
    return ""

def initial_default_fields(Dirs, kwargs, super_class):
    with open(Dirs["Project_files"]["DefaultFields"][0], 'w') as f:
        f.write(field_templates.Header.ABSTRACT_CLASS_NAME["DefaultFields"])
        for item in super_class:
            if item[1] in ["ForeignKeyABC","GenericForeignKeyABC","GenericRelationABC"]:
                f.write(field_templates.Header.ABSTRACT_CLASS_NAME[str(item[1])[:-3]])
                continue
            f.write(field_templates.Header.ABSTRACT_CLASS_NAME[str(item[1])[:-3]+"Fields"])
    return ""
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--p', '-project_name', type = str, help = 'Indicates Project name')
        parser.add_argument('--m', '-app_model_list', nargs = '*', help = 'Indicates App Models List Name')
        parser.add_argument('--s', '-app_scope_parent', type = str, help = 'Indicates App Scope Parent name')
        parser.add_argument('--D', '-delete', default = False, const = True, nargs = '?', choices = [True, False], help = 'force delete for adding not existing files and classes\n')

        parser.add_argument('--F', '-file', default = "making_field.txt", const = "making_field.txt", nargs = "?", type = str, help = 'Indicates File name for batch in Core/management/AppMaker/...', required = True)

    def handle(self, *args, **kwargs):
        if not kwargs['F']:
            return "\n##attention##\nApp name required\n>->\texample : customstartapp --a=App_name --p=Project_name --m=Model1,Model2,Model3 --s=Scope_parent --o=option"
        delete = kwargs["D"]
        File = os.path.join(BASE_DIR, "Core", "management", "AppMaker", kwargs["F"])
        kwargs = Command.make_normal(kwargs)
        Dirs_Files = Command.get_os_files(kwargs)
        project_dir = Dirs_Files.pop("Project_dir")
        projectmixin = Dirs_Files.pop("Project_mixins")
        apps = Dirs_Files.pop("Apps")
        # {
        #     "App_files": App_files,
        #     "App_dirs": App_dirs,
        #     "Project_files": Project_files,
        #     "Project_dirs": Project_dirs
        #     }
        new = []
        print(Command.get_result(Dirs_Files))
        if delete == True:
            print("deleteing Dirs...")
            new += Command.make_files(Dirs_Files["Project_files"], app_name = kwargs["App_name"], delete = True)
            print("deleteing Files...")

            new += Command.make_dirs(Dirs_Files["Project_dirs"], app_name = kwargs["App_name"], delete = True)
        else:
            print("making dirs...\n")
            new += Command.make_dirs(Dirs_Files["Project_dirs"], app_name = kwargs["App_name"])
            print("making files...\n")
            new += Command.make_files(Dirs_Files["Project_files"], app_name = kwargs["App_name"])
            print("initialize required files")
            new += Command.initial_files(Dirs_Files["Project_files"], app_name = kwargs["App_name"])
        print(*new, sep = "\n")
        if delete == False:
            print("making classes...\n")
            new += Command.make_classes(Dirs_Files, kwargs, File)

    @staticmethod
    def make_classes(Dirs, kwargs, File):
        new = []
        super_class, sub_class = readfile(File)
        # print(*super_class, sep = "\n")
        # print(*sub_class, sep = "\n")
        # print(*sorted(super_class), sep = "\n")
        new += initial_default_fields(Dirs, kwargs, super_class)
        for sub in sub_class:
            new += make_sub_class(Dirs, kwargs, sub[0], sub[1])
        # print(*super_class,sep="\n")
        # print(*sub_class,sep="\n")
        # nwith open(File ,)= admin_maker(File = Dirs["App_files"]["Admin_py"][0], Models = kwargs["App_model_list"], App_name = kwargs["App_name"], Scope_parent = kwargs["App_scope_parent"], Option = kwargs["Option"])
        return new

    @staticmethod
    def get_os_files(kwargs):
        Dirs = {}
        Dirs["ProjectNameApp"] = (os.path.join(BASE_DIR, kwargs["Project_name"]))

        #####
        Dirs["Core"] = os.path.join(BASE_DIR, "Test")
        Dirs["ProjectMixins"]=os.path.join(Dirs["Core"], "ProjectMixins")
        Dirs["Apps"] = os.path.join(Dirs["ProjectMixins"], "Apps")
        Dirs["Base"]= os.path.join(Dirs["ProjectMixins"], "Base")

        Dirs["initpy_Base"]=os.path.join(Dirs["Base"], "__init__.py")
        Dirs["AbsoluteUrl"]=os.path.join(Dirs["Base"],"AbsoluteUrl.py")
        Dirs["ModelForeigns"]=os.path.join(Dirs["Base"],"ModelForeigns.py")
        Dirs["Save"]=os.path.join(Dirs["Base"],"Save.py")
        Dirs["Str"]=os.path.join(Dirs["Base"],"Str.py")

        Dirs["Fields"] = os.path.join(Dirs["Core"], "fields")

        ####
        Dirs["initpy_fields"] = os.path.join(Dirs["Fields"], "__init__.py")
        Dirs["BigAutoFields"] = os.path.join(Dirs["Fields"], "BigAutoFields.py")
        Dirs["BigIntegerFields"] = os.path.join(Dirs["Fields"], "BigIntegerFields.py")

        Dirs["BoleanFields"] = os.path.join(Dirs["Fields"], "BoleanFields.py")
        Dirs["CharFields"] = os.path.join(Dirs["Fields"], "CharFields.py")
        Dirs["DateFields"] = os.path.join(Dirs["Fields"], "DateFields.py")
        Dirs["DecimalFields"] = os.path.join(Dirs["Fields"], "DecimalFields.py")
        Dirs["DefaultFields"] = os.path.join(Dirs["Fields"], "DefaultFields.py")
        Dirs["EmailFields"] = os.path.join(Dirs["Fields"], "EmailFields.py")
        Dirs["FilePathFields"] = os.path.join(Dirs["Fields"], "FilePathFields.py")
        Dirs["ForeignKey"] = os.path.join(Dirs["Fields"], "ForeignKey.py")
        Dirs["GenericForeignKey"] = os.path.join(Dirs["Fields"], "GenericForeignKey.py")
        Dirs["GenericRelation"] = os.path.join(Dirs["Fields"], "GenericRelation.py")
        Dirs["FileFields"] = os.path.join(Dirs["Fields"], "FileFields.py")
        Dirs["ManyToManyFields"] = os.path.join(Dirs["Fields"], "ManyToManyFields.py")
        Dirs["OneToOneFields"] = os.path.join(Dirs["Fields"], "OneToOneFields.py")
        Dirs["PositiveIntegerFields"] = os.path.join(Dirs["Fields"], "PositiveIntegerFields.py")
        Dirs["ProjectFields"] = os.path.join(Dirs["Fields"], "ProjectFields.py")
        Dirs["SlugFields"] = os.path.join(Dirs["Fields"], "SlugFields.py")
        Dirs["TextFields"] = os.path.join(Dirs["Fields"], "TextFields.py")
        Dirs["TimeFields"] = os.path.join(Dirs["Fields"], "TimeFields.py")

        for key, value in Dirs.items():
            Dirs[key] = tuple([value, os.path.exists(value)])
        project_files = Dirs
        project_dirs = {}
        project_dirs["Fields"] = project_files.pop("Fields")
        project_dirs["Core"] = project_files.pop("Core")

        project_dirs["Base"] = project_files.pop("Base")
        apps = project_files.pop("Apps")
        Project_dir = project_files.pop("ProjectNameApp")
        project_mixins =project_files.pop("ProjectMixins")

        return {
            "Project_files": project_files,
            "Project_dirs": project_dirs,
            "Project_dir": Project_dir,
            "Project_mixins":project_mixins,
            "Apps":apps,
            }

    @staticmethod
    def get_project_name():
        if os.path.exists(os.path.join(BASE_DIR, "manage.py")):
            result = str(BASE_DIR).split("\\")[-1]
            return result

    @staticmethod
    def get_models_name():
        return ["TestModelFromCommandLine"]

    @staticmethod
    def get_scope_parent():
        return "TestModelScopeParentFromCommandLine"

    @staticmethod
    def make_normal(kwargs):
        Project_name = kwargs.get("p", None)
        if Project_name is None:
            Project_name = Command.get_project_name()
        del kwargs
        kwargs = {
            "App_name": "Test",
            "Project_name": Project_name,
            }
        return kwargs

    @staticmethod
    def get_result(Dirs):
        try:
            result = "****************************************************************************************************\n"
            for yek, eulave in Dirs.items():
                Title = yek
                result = result + Title + "\n"
                for key, value in eulave.items():
                    result = result + f"{str(key):>30} : exist : {str(value[1]):5} : {str(value[0])} \n"
                result += "****************************************************************************************************\n"
            return result
        except:
            result = "****************************************************************************************************\n"
            for key, value in Dirs.items():
                result = result + f"{str(key):>30} : exist : {str(value[1]):5} : {str(value[0])} \n"
            result += "****************************************************************************************************\n"

        return result

    @staticmethod
    def make_dirs(Dirs, app_name, delete = False):
        result = []
        if delete == True:
            for key, value in Dirs.items():
                if value[1]:
                    try:
                        shutil.rmtree(value[0])
                        result.append(f"{key:30} " + " Deleted from\t...\t" + value[0])
                    except:
                        pass
        else:
            for key, value in Dirs.items():
                if key == "Core": continue

                if not value[1]:
                    os.makedirs(value[0])
                    result.append(f"{key:30} " + " Created   at  \t...\t" + value[0])
        return result

    @staticmethod
    def make_files(Files, app_name, delete = False):
        result = []
        if delete == True:
            for key, value in Files.items():
                if value[1]:
                    try:
                        os.remove(value[0])
                        result.append(f"{key:30} " + " Deleted   at\t...\t" + value[0])
                    except:
                        pass
        else:
            for key, value in Files.items():
                if not value[1]:
                    with open(value[0], "w") as f:
                        f.write("")
                    result.append(f"{key:30} " + " Created   at\t...\t" + value[0])

        return result

    @classmethod
    def initial_files(cls, project_files, app_name):
        result =[]
        project_files_dict=dict(project_files.items())
        project_files_dict_keys = project_files_dict.keys()
        for file_name,file_content in dict(REQUIRED.REQUIRED_FILE_NAMES.items()).items():
            if file_name in project_files_dict_keys:
                with open(str(project_files_dict[file_name][0]), "w") as f:
                    f.write(file_content.format(app_name=app_name))
                    result.append(f"{file_name:30} " + " initialized at\t" + project_files_dict[file_name][0])
        return result

