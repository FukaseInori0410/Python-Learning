x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Global x is changed to', x)


func()
print('x is', x, 'now')