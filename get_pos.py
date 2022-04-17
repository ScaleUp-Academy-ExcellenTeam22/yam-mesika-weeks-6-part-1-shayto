def get_positive_numbers() -> list:
    """
    Function to read inputed_numbers separated by a comma from user and returns all the positive inputed_numbers.
    :return: positive inputed_numbers.
    """
    inputed_numbers = input("enter numbers separated by comma:")
    inputed_numbers = inputed_numbers.split(",")
    inputed_numbers = [number for number in inputed_numbers if int(number) > 0]
    return inputed_numbers


if __name__ == "__main__":
    print(get_positive_numbers())