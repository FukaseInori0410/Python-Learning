def print_max(a, b):
    """Prints the maximum of two numbers.

    The two values must be integers."""
    a = int(a)
    b = int(b)

    if a > b:
        print(a, 'is the maximum')
    else:
        print(b, 'is the maximum')


print_max(3, 5)
print(print_max.__doc__)

help(print_max)
