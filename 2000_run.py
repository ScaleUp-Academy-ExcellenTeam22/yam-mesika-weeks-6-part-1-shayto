import time


def timer(function, *args, **kwargs) -> float:
    """
    This function receives a function and parameters and calculates the time it takes for the
    to run with the parameters.
    :param function: The function.
    :param args: Parameters to the function.
    :param kwargs: Parameters to the function.
    :return: The time it took for the function to run.
    """
    start = time.time()
    function(*args, **kwargs)
    end = time.time()
    return end - start


if __name__ == "__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
