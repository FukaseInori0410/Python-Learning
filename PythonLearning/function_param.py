def print_max(a, b):
    if a > b:
        print(a, 'is bigger.')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is bigger.')


print_max(3, 3)

x = 1
y = 5
print_max(x, y)