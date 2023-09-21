#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list.
    Args:
    my_list: A list of integers.
    """
    if not my_list:
        print("The list is empty.")
        return
    for integer in my_list:
        print(str.format("{} ", integer))
