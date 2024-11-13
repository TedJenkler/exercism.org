"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):    
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    if convert_coordinate(azara_record[1]) == rui_record[1]:
        return True
    else:
        return False


def create_record(azara_record, rui_record):
    match = compare_records(azara_record, rui_record)
    if match:
        return (azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2])
    else:
        return "not a match"
        


def clean_up(combined_record_group):
    report = []
    
    for record in combined_record_group:
        treasure, _, location, coordinate, quadrant = record
        cleaned_record = (treasure, location, coordinate, quadrant)
        report.append(f"{cleaned_record}")
    return '\n'.join(report) + '\n'