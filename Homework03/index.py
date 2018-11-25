import simplegui

total_stops = 0
successful_stops = 0
timer_tick = 0
score = "0/0"



def format(t):
    A = str(t // 600)
    B = str(t // 100 % 6 )
    C = str(t % 100 / 10)
    D = str(t % 10)
    return A + ":" + B + C + "." + D


def start():
    global  score
    timer.start()
    score = str(successful_stops) + "/" + str(total_stops)
    
    
def stop():
    global total_stops, successful_stops, score, timer_tick
    timer.stop()
    msec = '.0'
    if msec in format(timer_tick):
        successful_stops += 1
    else:
        total_stops += 1
    score = str(successful_stops) + "/" + str(total_stops)

    
def reset():
    global score, total_stops, successful_stops, timer_tick
    total_stops = 0
    successful_stops = 0
    timer_tick = 0
    score = str(successful_stops) + "/" + str(total_stops)
    timer.stop()

    
def timer():
    global timer_tick
    if timer_tick < 6000:
        timer_tick +=1
    
    
def draw(canvas):
    canvas.draw_text(format(timer_tick),  (45, 110), 50, 'Green')
    canvas.draw_text(str(score), (160, 27), 25, 'White')

    
# create frame
frame = simplegui.create_frame('Stopwatch: Game', 200, 200)
frame.set_canvas_background("Black")
timer = simplegui.create_timer(100, timer)
frame.set_draw_handler(draw)


frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)	
frame.add_button("Reset", reset, 200)

frame.start()

