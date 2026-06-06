numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

import random
number=random.choice(numbers)

while True: 
    guess=input("Guess the number I chose from 1 to 10: ") 
    if guess.isdigit(): 
        guess=int(guess)
        if guess>10:
            print("Your guess must be a number between 1 and 10")
        if guess<1 :
            print("Your guess must be a number between 1 and 10")
        if guess!=number and 1<=guess<=10:
            print("Mmmm, not quite, try again!")
        if guess==number and 1<=guess<=10:
            print("You got it right!!!!")
            break
    else:
        print("Choose a number")
