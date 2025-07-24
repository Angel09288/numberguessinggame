import random
import math
secret_number = round(random.random() * 10)

attemps = 3

print("You have 3 attemps to guess the number")


for i in range(attemps):
    guess = int(input("Enter you guess: "))
if guess < secret_number:
    print(" Your number is too low")
elif guess > secret_number:
    print("Your number is too high")
elif guess == secret_number:
    print("You got it correct!")
    
else:
    print(f"Your out of guesses the correct answer was (secret_number)")
    print("Game Over")
    





guess+= 1 