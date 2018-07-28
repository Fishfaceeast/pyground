number = 23
guess = int(input('Enter a integer: '))

if guess == number:
    print("Congratulations. u guess it!")
elif guess < number:
    print("A little bit lower!")
else:
    print("A little bit higher!")