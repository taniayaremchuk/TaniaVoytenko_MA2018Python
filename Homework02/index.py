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
user_guess = 7
secret_number = 0
num_guesses = 7

# function to start and restart the game
def new_game():  
    global secret_number
    secret_number = random.randrange(0, num_range)
 
    global num_guesses
    num_guesses = math.log(num_range - 0 + 1) / math.log(2)
    num_guesses = int(math.ceil(num_guesses))
      
    print ("")
    print ("New game. Guess the number from 0 to"), num_range, (".\n")
    print ("Number of remaining guesses is"), num_guesses, (".\n")
    return None

def range100():
    global num_range
    num_range = 100 # button that changes range to range [0,100)
    new_game()
    return None

def range1000():
    global num_range
    num_range = 1000 # button that changes range to range [0,1000)
    new_game()
    return None

def input_guess(guess):
    
    game = False
    
    global user_guess
    user_guess = int(guess)
    print ("")
    print ("Your number ") + guess    
    global num_guesses 
    num_guesses  = num_guesses  - 1 
    if (num_guesses == 0):
        game = True                
    if (secret_number < user_guess): 
        if (num_guesses > 0):
            print ("Lower!")
            print ("Number of remaining guesses is "), str(num_guesses), (".")
        else:
            print ("You lose, the number was "), str(secret_number), (".")                                
    elif (secret_number > user_guess):
        if (num_guesses > 0):
            print ("Higher!")
            print ("Number of remaining guesses is "), str(num_guesses), (".")
        else:
            print ("Loser! The number was "), str(secret_number), ("!")
    else:
        print ("Correct!")
        
    game = True     
    if (game):
        new_game()
    
    return None

    
# create frame
frame = simplegui.create_frame("Guess the number!", 150, 150)
frame.set_canvas_background("Red")

# register handlers for control elements
frame.add_button("Range [0, 100)", range100, 200)
frame.add_button("Range [0, 1000)", range1000, 200)	
frame.add_input("Enter a guess", input_guess, 150)

# start new_game and frame
new_game()
frame.start()# Testing template for "Guess the number"

###################################################
# Student should add code for "Guess the number" here


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

num_range = 100
user_guess = 7
secret_number = 0
num_guesses = 7

# function to start and restart the game
def new_game():  
    global secret_number
    secret_number = random.randrange(0, num_range)
 
    global num_guesses
    num_guesses = math.log(num_range - 0 + 1) / math.log(2)
    num_guesses = int(math.ceil(num_guesses))
      
    print ("")
    print ("New game. Guess the number from 0 to"), num_range, (".\n")
    print ("Number of remaining guesses is"), num_guesses, (".\n")
    return None

def range100():
    global num_range
    num_range = 100 # button that changes range to range [0,100)
    new_game()
    return None

def range1000():
    global num_range
    num_range = 1000 # button that changes range to range [0,1000)
    new_game()
    return None

def input_guess(guess):
    
    game = False
    
    global user_guess
    user_guess = int(guess)
    print ("")
    print ("Your number ") + guess    
    global num_guesses 
    num_guesses  = num_guesses  - 1 
    if (num_guesses == 0):
        game = True                
    if (secret_number < user_guess): 
        if (num_guesses > 0):
            print ("Lower!")
            print ("Number of remaining guesses is "), str(num_guesses), (".")
        else:
            print ("You lose, the number was "), str(secret_number), (".")                                
    elif (secret_number > user_guess):
        if (num_guesses > 0):
            print ("Higher!")
            print ("Number of remaining guesses is "), str(num_guesses), (".")
        else:
            print ("Loser! The number was "), str(secret_number), ("!")
    else:
        print ("Correct!")
        
    game = True     
    if (game):
        new_game()
    
    return None

    
# create frame
frame = simplegui.create_frame("Guess the number!", 150, 150)
frame.set_canvas_background("Red")

# register handlers for control elements
frame.add_button("Range [0, 100)", range100, 200)
frame.add_button("Range [0, 1000)", range1000, 200)	
frame.add_input("Enter a guess", input_guess, 150)

# start new_game and frame
new_game()
frame.start()
