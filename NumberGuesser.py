import random

print("I am thinking of a number between 0 and 20. \nCan you get it within 5 tries? Have a Try.")

number = random.randint(0, 20)

numberOfGuesses = 0
while numberOfGuesses < 5:
    guess = int(input("Take a guess: "))

    if guess < number:
        print("Sorry, your guess was too low. Try Again.")
        numberOfGuesses += 1
    elif guess > number:
        print("Sorry, your guess was too high. Try Again.")
        numberOfGuesses += 1
    elif guess == number:
        print("That's correct. Good Job!")
        print("You took {} guesses!".format(numberOfGuesses))
        break
    
if numberOfGuesses == 5:
    print("Sorry, you took more than 5 tries. The number was {}.".format(number))
    