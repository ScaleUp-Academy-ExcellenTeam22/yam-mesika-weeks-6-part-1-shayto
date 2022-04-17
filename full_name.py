def full_names(first_names: list[str], last_names: list[str], min_length: int = 0) -> list[str]:
    """
    This function receives lists of first and last names.
    The function changes the first letter upper case and makes all the combinations of possible full
    names.
    If min_length is received the names returned will be all the names with length >= to min_length.
    :param first_names: List of first names.
    :param last_names: List of last names.
    :param min_length: Optional, the min_length of names.
    :return: List of all possible full names.
    """
    first_names = [name.title() for name in first_names]
    last_names = [name.title() for name in last_names]
    full_name = [first + " " + last for first in first_names for last in last_names]
    full_name = [name for name in full_name if len(name) >= min_length]
    return full_name


if __name__ == "__main__":
    first_name = ['avi', 'moshe', 'yaakov']
    last_name = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_name, last_name))
    print(full_names(first_name, last_name, 10))
