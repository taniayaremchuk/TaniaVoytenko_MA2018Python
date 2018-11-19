# Testing template for "Guess the number"

###################################################
# Student should add code for "Guess the number" here


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

num_range = 100
secret_number = 0
user_guess = 0
num_guesses = 7

# function to start and restart the game
def new_game():  
    global num_range
    global secret_number
    global user_guess
    
    secret_number = random.randrange(0, num_range)
    
    if num_range == 100: 	
        user_guess = 7
    elif num_range == 1000:
        user_guess = 10
      

    print ("New game. Range is from 0 to"), num_range, (".\n")
    print ("Number of remaining guesses is"), user_guess, (".\n")


def decrement_guesses():
    global num_guesses
    num_guesses = num_guesses - 1
    if num_guesses > 0:
        print ("Remaining guesses: "), str(num_guesses)
    else:
        print ("Loser! The number was "), str(secret_number),("!")
        new_game()

def range100():
    global num_range
    num_range = 100 # button that changes range to range [0,100)
    pass

def range1000():
    global num_range
    num_range = 1000 # button that changes range to range [0,1000)
    new_game()
    pass

def input_guess(guess):
    global secret_number, user_guess
    user_guess = int(guess)
    print ("")
    if user_guess == secret_number:
        print ("Your guess "), str(user_guess), (".")
        print ("You win!\n")
        new_game()
    elif user_guess > secret_number:
        print ("Your guess "), str(user_guess), (".")
        print ("Lower!")
    elif user_guess < secret_number:
        print ("Your guess "), str(user_guess), (".")
        print ("Higher!") 
    else:
        print ("Error!")
    decrement_guesses()
    
# create frame
frame = simplegui.create_frame("Guess the number!", 150, 150)
frame.set_canvas_background("Red")

# register handlers for control elements
frame.add_button("Range [0, 100)", range100, 200)
frame.add_button("Range [0, 1000)", range1000, 200)	
frame.add_input("Enter guess", input_guess, 150)

# start new_game and frame
new_game()
frame.start()