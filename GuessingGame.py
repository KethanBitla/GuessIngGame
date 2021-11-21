import random

def guessing_game(guessCounter,number):
    random_number = random.randint(1,number)
    try:
        while guessCounter > 0 :
            guess = int(input("What is your guess?"))
            guessCounter = guessCounter - 1
            if random_number == guess :
                print("Yours guess is right,You won the game.")
                return
            elif guess > number :
                print("Your Guess is out of range")
                print(f'You have {guessCounter} guess(es) left')
            else:
                print("Sorry That was wrong!")
                print(f'You have {guessCounter} guess(es) left')
        print("Game Over!")
        print(f'the random number was {random_number}')
    except valueError:
        print('Enter a valid number')

def easy():
    print("You are to guess a number between 1 and 10, and you have 6 guesses")
    guessing_game(6,10)

def medium():
    print("You are to guess a number between 1 and 20, and you have 4 guesses")
    guessing_game(4,20)

def hard():
    print("You are to guess a numer between 1 and 50, and you have 3 guesses")
    guessing_game(3,50)

def try_again():
    again = input("Do you want to play again?(Yes/No)")
    if again.upper() == 'YES':
        welcome()
    elif again.upper() == 'NO':
        print("Thanks For Playing.")
    else:
        print("Wrong Input")
        try_again()

def welcome():
    print("Welcome to the Guessing Game")
    difficulty = input("Choose your difficulty between\nEasy\nMedium\nhard\n")
    if difficulty.upper() == 'EASY':
        easy()
        try_again()
    elif difficulty.upper() == 'MEDIUM':
        medium()
        try_again()
    elif difficulty.upper() == 'HARD':
        hard()
        try_again()
    else:
        print("Choose a Valid diffiulty level between the given options")
        welcome()

welcome()
