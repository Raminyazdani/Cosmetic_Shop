def ModelProperty_maker(File, Models, App_name, Scope_parent, Option):
    result = []

    with open(File, "w") as f:
        body_required_fields = f"""
        
    """
        body_search_fields = f"""
        
    """
        for Model in Models:
            body_required_fields += f"""
    {Model.upper()} = []
    """

            body_search_fields += f"""
    {Model.upper()}_search_fields = []
    """

            result.append(f"{App_name:10}.{Model.capitalize():>25}\t {'RequiredFields':25} \t\tadded in ModelProperty.py")
            result.append(f"{App_name:10}.{Model.capitalize():>25}\t {'SearchFields':25} \t\tadded in ModelProperty.py")
        body = f"""
class REQUIREDFIELDS:
    {body_required_fields}
class SEARCHFIELDS:
    {body_search_fields}
"""

        f.write(body)
    return result
