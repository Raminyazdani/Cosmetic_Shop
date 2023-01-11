from Core.management.commands.ManagerUtils.CheckLines import check_lines_inside
from Core.management.commands.ManagerUtils.RemoveEmptyLines import remove_empty_lines

def ModelProperty_maker(File, Models, App_name, Scope_parent, Option):
    result = []
    remove_empty_lines(File)
    Header_Req, Header_Search = "REQUIREDFIELDS", "SEARCHFIELDS"
    Models_Req, temp_req = check_lines_inside(File, Models, App_name, Scope_parent, header = Header_Req, prefix = "")
    Models_Search, temp_search = check_lines_inside(File, Models, App_name, Scope_parent, header = Header_Search, prefix = "")
    # required
    with open(File, "w") as f:
        if Option == "hard":
            f.write(f"class {Header_Req}:\n")
            for Model in Models:
                f.write(f"    {Model.upper()} = []\n")
                result.append(f"{App_name:10}.{Model.capitalize():<25}\t {'RequiredFields':25} \t\tadded in ModelProperty.py")
            f.write(f"class {Header_Search}:\n")
            for Model in Models:
                f.write(f"    {Model.upper()} = []\n")
                result.append(f"{App_name:10}.{Model.capitalize():<25}\t {'RequiredFields':25} \t\tadded in ModelProperty.py")
        if Option == "soft":
            f.write(f"class {Header_Req}:\n")
            f.writelines(temp_req)
            for Model in Models_Req:
                f.write(f"    {Model.upper()} = []\n")
                result.append(f"{App_name:10}.{Model.capitalize():<25}\t {'RequiredFields':25} \t\tadded in ModelProperty.py")
            f.write(f"class {Header_Search}:\n")
            f.writelines(temp_search)
            for Model in Models_Search:
                f.write(f"    {Model.upper()} = []\n")
                result.append(f"{App_name:10}.{Model.capitalize():<25}\t {'RequiredFields':25} \t\tadded in ModelProperty.py")
    return result
