# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # convert name to number using if/elif/else 
    if name == ("rock"):
        result = 0
    elif name == ("Spock"):
        result = 1
    elif name == ("paper"):
        result = 2
    elif name == ("lizard"):
        result = 3
    elif name == ("scissors"):
        result = 4
    return result    


def number_to_name(number):
    # convert number to a name using if/elif/else  
    if number == 0:
        result = ("rock")
    elif number == 1:
        result = ("Spock")
    elif number == 2:
        result = ("paper")
    elif number == 3:
        result = ("lizard")
    elif number== 4:
        result = ("scissors")
    return result 


def rpsls(player_choice): 
    print ("")
    player_number = name_to_number(player_choice)
    print ("Player chooses"), player_choice
    
    comp_number = random.randrange(0,5)
    
    print ("Computer chooses"), number_to_name(comp_number)
   
    if (comp_number + 1) % 5 == player_number:
        print ("Player wins!")
    elif (comp_number + 2) % 5 == player_number:
        print ("Player wins!")
    elif comp_number == player_number:
        print ("Player and computer tie!")
    else:
        print ("Computer wins!")



    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


