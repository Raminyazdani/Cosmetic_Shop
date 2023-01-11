import os
import shutil

from django.core.management import execute_from_command_line
from django.core.management.base import BaseCommand, CommandError

from Core.management.commands.ManagerUtils.AdminProperty_maker import AdminProperty_maker
from Core.management.commands.ManagerUtils.ModelForeigns_maker import ModelForeigns_maker
from Core.management.commands.ManagerUtils.ModelMethods_maker import ModelMethods_maker
from Core.management.commands.ManagerUtils.ModelProperty_maker import ModelProperty_maker
from Core.management.commands.ManagerUtils.ModelRequiredProperties_maker import ModelRequiredProperties_maker
from Core.management.commands.ManagerUtils.admin_maker import admin_maker
from Core.management.commands.ManagerUtils.models_maker import models_maker
from Cosmetic_Shop.settings import BASE_DIR

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--a', '-app_name', type = str, help = 'Indicates App name')
        parser.add_argument('--p', '-project_name', type = str, help = 'Indicates Project name')
        parser.add_argument('--m', '-app_model_list', nargs = '*', help = 'Indicates App Models List Name')
        parser.add_argument('--s', '-app_scope_parent', type = str, help = 'Indicates App Scope Parent name')
        parser.add_argument('--o', '-option', default = 'soft', const = 'soft', nargs = '?', choices = ['soft', 'hard', 'delete', 'from'], help = 'soft for adding not existing files and classes\n'
                                                                                                                                                  'hard for adding and overwriting files and classes\n'
                                                                                                                                                  'delete for deleting files and classes\n'
                                                                                                                                                  'from for getting files and classes from a text file for batch')
        parser.add_argument('--f', '-file', default = "making.txt", const = "making.txt", nargs = "?", type = str, help = 'Indicates File name for batch in Core/management/AppMaker/...')
        parser.add_argument('--D', '-delete', default = False, const = True, nargs = '?', choices = [True, False], help = 'force delete for adding not existing files and classes\n')
        parser.add_argument('--H', '-hard', default = False, const = True, nargs = '?', choices = [True, False], help = 'force hard for adding not existing files and classes\n')
        parser.add_argument('--S', '-soft', default = False, const = True, nargs = '?', choices = [True, False], help = 'force soft for adding not existing files and classes\n')

    def handle(self, *args, **kwargs):
        if kwargs['o'] == 'from':
            if kwargs['f'] is None:
                print('Please enter file name and path')
                return
            else:
                destination = os.path.join(BASE_DIR, 'Core', 'management', 'AppMaker', kwargs['f'])
                print("destination is :", destination)
                with open(destination, 'r') as f:
                    formated_apps = []
                    for line in f.readlines():
                        if line[0] == '#':
                            continue
                        line = line.split()
                        if len(line) == 5:
                            app_name, project_name, app_model_list, app_scope_parent, option = line
                            formated_apps.append(app_name)
                            app_model_list = app_model_list.split(',')
                            kwargs_init = {
                                "app_name": app_name,
                                "project_name": project_name,
                                "app_model_list": " ".join(app_model_list),
                                "app_scope_parent": app_scope_parent,
                                "option": option,
                                }
                            execution_list = ["manage.py", "customstartapp", "--a", app_name, "--p", project_name, "--m"]
                            [execution_list.append(model) for model in app_model_list]
                            if kwargs["D"] == True:
                                execution_list.extend(["--s", app_scope_parent, "--o", "delete"])
                            elif kwargs["H"] == True:
                                execution_list.extend(["--s", app_scope_parent, "--o", "hard"])
                            elif kwargs["S"] == True:
                                execution_list.extend(["--s", app_scope_parent, "--o", "soft"])
                            else:
                                execution_list.extend(["--s", app_scope_parent, "--o", option])

                            execute_from_command_line(execution_list)

                        else:
                            print('Please check your file format')
                            return
                return "Files and Classes are created for the following apps: {}".format(formated_apps)

        if not kwargs['a']:
            return "\n##attention##\nApp name required\n>->\texample : customstartapp --a=App_name --p=Project_name --m=Model1,Model2,Model3 --s=Scope_parent --o=option"
        kwargs = Command.make_normal(kwargs)

        try:
            execute_from_command_line(["manage.py", "startapp", kwargs["App_name"]])
            self.stdout.write(kwargs["App_name"] + "App Base Creation Completed")
        except CommandError:
            self.stdout.write(kwargs["App_name"] + "App Base Existed")
        finally:  # self.stdout.write(result)
            Dirs_Files = Command.get_os_files(kwargs)
            # {
            #     "App_files": App_files,
            #     "App_dirs": App_dirs,
            #     "Project_files": Project_files,
            #     "Project_dirs": Project_dirs
            #     }
            new = []
            print(Command.get_result(Dirs_Files))
            if kwargs["Option"] == "delete":
                new += Command.make_files(Dirs_Files["App_files"], option = kwargs["Option"], app_name = kwargs["App_name"])
                new += Command.make_dirs(Dirs_Files["App_dirs"], option = kwargs["Option"], app_name = kwargs["App_name"])
            else:
                new += Command.make_dirs(Dirs_Files["Project_dirs"], option = "soft", app_name = kwargs["App_name"])
                new += Command.make_dirs(Dirs_Files["App_dirs"], option = kwargs["Option"], app_name = kwargs["App_name"])
                new += Command.make_files(Dirs_Files["App_files"], option = kwargs["Option"], app_name = kwargs["App_name"])
                new += Command.make_files(Dirs_Files["Project_files"], option = "soft", app_name = kwargs["App_name"])
                if kwargs["Option"] in ["soft", "hard"]:
                    new += Command.model_initialize(Dirs_Files, kwargs)
                else:
                    print("done")
            print(*new, sep = "\n")

    @staticmethod
    def model_initialize(Dirs, kwargs):
        new = []
        kwargs['App_model_list'] = [x.capitalize() for x in kwargs['App_model_list']]
        new += admin_maker(File = Dirs["App_files"]["Admin_py"][0], Models = kwargs["App_model_list"], App_name = kwargs["App_name"], Scope_parent = kwargs["App_scope_parent"], Option = kwargs["Option"])
        new += AdminProperty_maker(File = Dirs["App_files"]["AdminProperty"][0], Models = kwargs["App_model_list"], App_name = kwargs["App_name"], Scope_parent = kwargs["App_scope_parent"], Option = kwargs["Option"])
        new += ModelForeigns_maker(File = Dirs["App_files"]["ModelForeigns"][0], Models = kwargs["App_model_list"], App_name = kwargs["App_name"], Scope_parent = kwargs["App_scope_parent"], Option = kwargs["Option"])
        new += ModelMethods_maker(File = Dirs["App_files"]["ModelMethods"][0], Models = kwargs["App_model_list"], App_name = kwargs["App_name"], Scope_parent = kwargs["App_scope_parent"], Option = kwargs["Option"])
        new += ModelProperty_maker(File = Dirs["App_files"]["ModelProperty"][0], Models = kwargs["App_model_list"], App_name = kwargs["App_name"], Scope_parent = kwargs["App_scope_parent"], Option = kwargs["Option"])
        new += ModelRequiredProperties_maker(File = Dirs["App_files"]["ModelRequiredProperties"][0], Models = kwargs["App_model_list"], App_name = kwargs["App_name"], Scope_parent = kwargs["App_scope_parent"], Option = kwargs["Option"])
        new += models_maker(File = Dirs["App_files"]["Models_py"][0], Models = kwargs["App_model_list"], App_name = kwargs["App_name"], Scope_parent = kwargs["App_scope_parent"], Option = kwargs["Option"])
        return new

    @staticmethod
    def get_os_files(kwargs):
        Dirs = {}
        Dirs["ProjectNameApp"] = (os.path.join(BASE_DIR, kwargs["Project_name"]))

        #####
        Dirs["Setting"] = os.path.join(Dirs["ProjectNameApp"], "settings.py")

        Dirs["Core"] = os.path.join(BASE_DIR, "Core")
        Dirs["ProjectMixins"] = os.path.join(Dirs["Core"], "ProjectMixins")
        Dirs["Apps"] = os.path.join(Dirs["ProjectMixins"], "Apps")

        ####
        Dirs["ProjectMixinsAppDir"] = os.path.join(Dirs["Apps"], kwargs["App_name"] + "_Mixins")

        Dirs["initpy"] = os.path.join(Dirs["ProjectMixinsAppDir"], "__init__.py")
        Dirs["AdminProperty"] = os.path.join(Dirs["ProjectMixinsAppDir"], "AdminProperty.py")
        Dirs["ModelForeigns"] = os.path.join(Dirs["ProjectMixinsAppDir"], "ModelForeigns.py")
        Dirs["ModelMethods"] = os.path.join(Dirs["ProjectMixinsAppDir"], "ModelMethods.py")
        Dirs["ModelProperty"] = os.path.join(Dirs["ProjectMixinsAppDir"], "ModelProperty.py")
        Dirs["ModelRequiredProperties"] = os.path.join(Dirs["ProjectMixinsAppDir"], "ModelRequiredProperties.py")
        Dirs["AppDir"] = os.path.join(BASE_DIR, kwargs["App_name"])
        Dirs["Admin_py"] = os.path.join(Dirs["AppDir"], "admin.py")
        Dirs["Models_py"] = os.path.join(Dirs["AppDir"], "models.py")
        for key, value in Dirs.items():
            Dirs[key] = tuple([value, os.path.exists(value)])
        Project = {}
        Project["ProjectNameApp"] = Dirs.pop("ProjectNameApp")
        Project["Setting"] = Dirs.pop("Setting")
        Project["Core"] = Dirs.pop("Core")
        Project["ProjectMixins"] = Dirs.pop("ProjectMixins")
        Project["Apps"] = Dirs.pop("Apps")
        App_files = Dirs
        Project_dirs = Project
        Project_files = {}
        Project_files["Setting"] = Project_dirs.pop("Setting")
        App_dirs = {}
        App_dirs["ProjectMixinsAppDir"] = App_files.pop("ProjectMixinsAppDir")
        App_dirs["AppDir"] = App_files.pop("AppDir")

        return {
            "App_files": App_files,
            "App_dirs": App_dirs,
            "Project_files": Project_files,
            "Project_dirs": Project_dirs
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
        App_name = kwargs['a']
        if App_name is None:
            return print("App name is required")
        Project_name = kwargs.get("p", None)
        if Project_name is None:
            Project_name = Command.get_project_name()
        App_model_list = kwargs.get('m', None)
        if App_model_list is None:
            App_model_list = Command.get_models_name()
        App_scope_parent = kwargs.get('s', None)
        if App_scope_parent is None:
            App_scope_parent = Command.get_scope_parent()
        Option = kwargs.get('o')
        del kwargs
        kwargs = {
            "App_name": App_name,
            "Project_name": Project_name,
            "App_model_list": App_model_list,
            "App_scope_parent": App_scope_parent,
            "Option": Option
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
    def make_dirs(Dirs, option, app_name):
        result = []
        if option == "soft":
            for key, value in Dirs.items():
                if not value[1]:
                    os.makedirs(value[0])
                    result.append(f"{app_name:10}\t{key:30} " + " Created at\t...\t" + value[0])

        elif option == "hard":
            for key, value in Dirs.items():
                if value[1]:
                    shutil.rmtree(value[0])
                os.makedirs(value[0])
                result.append(f"{app_name:10}\t{key:30} " + " Created at\t...\t" + value[0])
        elif option == "delete":
            for key, value in Dirs.items():
                if value[1]:
                    shutil.rmtree(value[0])
                    result.append(f"{app_name:10}\t{key:30} " + " Deleted from\t...\t" + value[0])
        #  from option
        elif option == "from":
            pass
        return result

    @staticmethod
    def make_files(Dirs, option, app_name):
        result = []
        if option == "soft":
            for key, value in Dirs.items():
                if not value[1]:
                    with open(value[0], "w") as f:
                        f.write("")
                    result.append(f"{app_name:10}\t{key:30} " + " Created at\t...\t" + value[0])

        elif option == "hard":
            for key, value in Dirs.items():
                if value[1]:
                    os.remove(value[0])
                with open(value[0], "w") as f:
                    f.write("")
                result.append(f"{app_name:10}\t{key:30} " + " Created at\t...\t" + value[0])
        elif option == "delete":
            for key, value in Dirs.items():
                if value[1]:
                    os.remove(value[0])
                    result.append(f"{app_name:10}\t{key:30} " + " Deleted from\t...\t" + value[0])
        # : from option
        elif option == "from":
            pass
        return result
