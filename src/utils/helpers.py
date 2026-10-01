def format_name(name):
    return name.strip().title()


def is_active(status):
    return status.lower() == "active"


def calculate_percentage(value, percentage):
    return value * percentage / 100