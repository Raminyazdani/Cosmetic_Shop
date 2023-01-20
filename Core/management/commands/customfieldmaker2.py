import os
import re

from django.core.management import BaseCommand

def find_base_dir():
    """Find the base directory of the project"""
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    return base_dir

def find_file_dir(BASE_DIR, FILE_DIR):
    return os.path.join(BASE_DIR, "Core", "management", "AppMaker", FILE_DIR)

def collect_field_data(FILE_DIR):
    class_regex = re.compile(r"^(\S+)")
    field_regex = re.compile(r"(\s{1,})(\S+)")
    data ={}
    with open(FILE_DIR, "r") as file:
        lines = file.readlines()

        for line in lines:
            if temp_head:=class_regex.match(line):
                head = temp_head.group(1)
                data[head] = []
            elif temp_subhead:=field_regex.match(line):
                subhead = temp_subhead.group(2)
                data[head].append(subhead)
    return sorted(data.items(), key=lambda x: x[0])

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--A', '-App', default = "Test", const = "Test", nargs = '?', help = 'App Name for init\n')
        parser.add_argument('--D', '-delete', default = False, const = True, nargs = '?', choices = [True, False], help = 'force delete for adding not existing files and classes\n')
        parser.add_argument('--F', '-file', default = "making_field.txt", const = "making_field.txt", nargs = "?", type = str, help = 'Indicates File name for batch in Core/management/AppMaker/...')

    def handle(self, *args, **kwargs):
        delete = kwargs["D"]
        App = kwargs["A"]
        FILE_DIR = kwargs["F"]
        BASE_DIR = find_base_dir()
        FILE_DIR = find_file_dir(BASE_DIR, FILE_DIR)
        FIELDS_DATA = collect_field_data(FILE_DIR)
        print(*FIELDS_DATA,sep = "\n")
        print(FILE_DIR)
        # kwargs = Command.make_normal(kwargs)
        # Dirs_Files = Command.get_os_files(kwargs)
        # project_dir = Dirs_Files.pop("Project_dir")
        # projectmixin = Dirs_Files.pop("Project_mixins")
        # apps = Dirs_Files.pop("Apps")
        # # {
        # #     "App_files": App_files,
        # #     "App_dirs": App_dirs,
        # #     "Project_files": Project_files,
        # #     "Project_dirs": Project_dirs
        # #     }
        # new = []
        # print(Command.get_result(Dirs_Files))
        # if delete == True:
        #     print("deleteing Dirs...")
        #     new += Command.make_files(Dirs_Files["Project_files"], app_name = kwargs["App_name"], delete = True)
        #     print("deleteing Files...")
        #
        #     new += Command.make_dirs(Dirs_Files["Project_dirs"], app_name = kwargs["App_name"], delete = True)
        # else:
        #     print("making dirs...\n")
        #     new += Command.make_dirs(Dirs_Files["Project_dirs"], app_name = kwargs["App_name"])
        #     print("making files...\n")
        #     new += Command.make_files(Dirs_Files["Project_files"], app_name = kwargs["App_name"])
        #     print("initialize required files")
        #     new += Command.initial_files(Dirs_Files["Project_files"], app_name = kwargs["App_name"])
        # print(*new, sep = "\n")
        # if delete == False:
        #     print("making classes...\n")
        #     new += Command.make_classes(Dirs_Files, kwargs, File)
