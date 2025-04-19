secret = 7 
guess = int(input("Guess a number between 1 and 10: "))
while guess != secret:
    print("Wrong!")
    guess = int(input("Try again: "))
print("Congratulations! You guessed the number.")
# This code is a simple number guessing game where the user has to guess a secret number between 1 and 10.