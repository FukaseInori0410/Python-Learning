number = 23
running = True

while running:
    guess = int(input('Enter an integer: '))
    if guess == number:
        print('Congratulations! You are right!')
        running = False
    elif guess < number:
        print('It is a little lower than what you guess ~')
    elif guess > number:
        print('It is a little higher than what you guess ~')
else:
    print('The while loop is over.')
print('Done.')

