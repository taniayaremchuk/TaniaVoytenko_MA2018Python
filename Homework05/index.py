# implementation of card game - Memory

import simplegui
import random

turns = 0
total_turns = 0
list1 = range(0, 8)
list2 = range(0, 8)
mdeck = list1 + list2

card_width = 50
card_height = 100

exposed = []
state = 0
# helper function to initialize globals
def new_game():
    global mdeck, exposed, total_turns, state, turns
   
    random.shuffle(mdeck)
    
    exposed = [0]*16
    total_turns = 0
    state = 0
    turns = [-1,-1]
    label.set_text("Turns = " + str(total_turns))
    
    # define event handlers
def mouseclick(pos):
    global turns, state, total_turns, card_width
    i = int(pos[0]/card_width)
    if state == 0:
        if exposed[i] == 0:
            if mdeck[turns[0]] != mdeck[turns[1]]:
                exposed[turns[0]] = 0
                exposed[turns[1]] = 0
            exposed[i] = 1
            state = 1
            turns[0] = i
    elif state == 1:
        if exposed[i] == 0:
            state = 0
            exposed[i] = 1
            turns[1] = i
            total_turns = total_turns + 1   
            label.set_text("Turns = " + str(total_turns))
            
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global mdeck, card_width, card_height
    for i in range(0,len(mdeck)):
        if exposed[i]==0 :
            canvas.draw_polygon([(card_width*i, 0), (card_width*(i+1), 0), (card_width*(i+1), 100), (card_width*i, 100)], 5, 'black', 'green')
        else:
            canvas.draw_text(str(mdeck[i]), [card_width*i+5, card_height-25], 70, 'white')
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
