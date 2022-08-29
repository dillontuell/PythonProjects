import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print("Hooray! You guessed the correct number!")

def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #this could also be high b/c low=high
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)??")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("Hooray, the computer guessed the correct number!")
computer_guess(10)