while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('The length is too small!')
        continue
    print('Length of the string is:', len(s))
print('Done')
