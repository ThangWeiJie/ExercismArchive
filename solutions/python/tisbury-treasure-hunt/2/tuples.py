"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[-1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    COORDINATE_INDEX = 1

    coord_one = convert_coordinate(get_coordinate(azara_record))
    coord_two = rui_record[COORDINATE_INDEX]

    return coord_one == coord_two


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if not compare_records(azara_record, rui_record):
        return "not a match"

    return azara_record + rui_record


def clean_up(combined_record_group):
    temp_list = []

    for items in combined_record_group:
        treasure = items[0]
        location = items[2]
        coordinates = items[3]
        quadrant = items[4]

        row = (treasure, location, coordinates, quadrant)
        temp_list.append(str(row))

    x = "\n".join(temp_list) + "\n"
    return x
