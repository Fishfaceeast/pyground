number = 23
running = True

while running:
    guess = int(input('Enter a integer: '))
    if guess == number:
        print("Congratulations. u guess it!")
        print('The loop is over')
        running = False
        break
    elif guess < number:
        print("A little bit lower!")
    else:
        print("A little bit higher!")
else:
    print('let me see if execute this')