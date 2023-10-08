#!/usr/bin/python3
"""Defines an integer addition function."""
def add_integer(a, b=98):
  """Adds two integers.
  Args:
    a: The first integer.
    b: The second integer. Defaults to 98.
  Returns:
    The sum of a and b.
  Raises:
    TypeError: If a or b is not an integer or float.
  """

def add_integer(a, b=98):
    """ add two integers or flots """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
