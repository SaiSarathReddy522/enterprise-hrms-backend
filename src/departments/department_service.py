def create_department(name, description):
    return {
        "name": name,
        "description": description
    }


def get_department(department):
    return department


def update_department(department, name=None, description=None):
    if name:
        department["name"] = name

    if description:
        department["description"] = description

    return department