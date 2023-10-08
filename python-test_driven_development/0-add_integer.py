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
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("a must be an integer or b must be an integer")
  a = int(a)
  b = int(b)
  return a + b
