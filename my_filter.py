from collections.abc import Iterable


def my_filter(func,  iterable: Iterable):
    """
    function that acts as regular python filter function.
    :param func: function that we want our new list to act by.
    :param iterable: iterable object (list, tuple etc..)
    :return: the new list
    """
    new_list = []
    for value in iterable:
        if func:
            if func(value):
                new_list.append(value)
        else:
            if value:
                new_list.append(value)
    return new_list


def is_mature(age):
    return age >= 18


if __name__ == "__main__":
    ages = [0, 1, 4, 10, 20, 35, 56, 84, 120]
    mature_ages = my_filter(is_mature, ages)
    print(tuple(mature_ages))
