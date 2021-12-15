number = 23
guess = int(input('Enter an integer: '))

if guess == number:
    print('Congratulations! You are right!')
elif guess < number:
    print('It is a little lower than what you guess ~')
elif guess > number:
    print('It is a little higher than what you guess ~')
print('Done')