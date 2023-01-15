import re

def check_lines(File, Models, App_name, Scope_parent, header,prefix):
    # regex_classes = re.compile(rf"^class\s*(.*){prefix}\s*(\(.*\))*:")
    regex_classes = re.compile(rf"^class\s*([^\s|\(:]*){prefix}\(?.*:?")
    regex_imports = re.compile(r"^(from|import)\s+([a-zA-Z0-9_.]+)\s*(as\s+[a-zA-Z0-9_]+)?")

    new_models = []

    all_classes_lines = []
    temp = []

    with open(File, "r") as f:
        lines = f.readlines()

        for line in lines:
            if regex_classes.match(line):
                all_classes_lines.append(regex_classes.match(line).group(1).strip())
            if not regex_imports.match(line):
                temp.append(line)
    with open(File, "w") as f:
        f.write(header)
        f.writelines(temp)
    for model in Models:
        if model not in all_classes_lines:
            new_models.append(model)
    return new_models

def check_lines_inside(File, Models, App_name, Scope_parent, header, prefix):
    regex_header = re.compile(rf"^class\s+(.*)\s*:")
    regex_classes= re.compile(rf"^\s+(.*)\s*\=")
    all_classes_model=[]
    all_classes_lines = []

    temp = []
    with open(File, "r") as f:
        lines = f.readlines()
        head =""
        for line in lines:
            if regex_header.match(line):
                head = regex_header.match(line).group(1).strip()
            if head == header:
                if regex_classes.match(line):
                    all_classes_lines.append(regex_classes.match(line).group(1).strip())
                    temp.append(line)
    new_models = []
    for Model in Models:
        if Model.upper() not in all_classes_lines:
            new_models.append(Model)


    return new_models,temp