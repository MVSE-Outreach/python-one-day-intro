def numberGuesser():
    import random
    print("Welcome to my guessing game")
    print("===========================")
    print()
    print("Can you guess the number (between 1 and 100) that the computer has chosen?")
    print()
    

    number = random.randint(1, 100)
    # create a random number   
    guess = -1    
    while guess != number:
        guess = int(input('Enter your guess : '))
        if guess == number:
            print('Congratulations, you guessed it.')
            guessed = True
        elif guess > number:
            print('Too high! Try again!')
        
        else:
            print('Too low! Try again!')
    print('Program over!')
