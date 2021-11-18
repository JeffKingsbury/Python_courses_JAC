import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from SimpleGUICS2Pygame.simpleguics2pygame import timer

# Global variables
counter_string = "00:00:0"
minutes = 0
seconds = 0
miliseconds = 0

# Methods


def start_counter():
    timer.start()


def stop_counter():
    timer.stop()


def reset_counter():
    global seconds, miliseconds, minutes, counter_string
    timer.stop()
    counter_string = "00:00:0"
    seconds = 0
    miliseconds = 0
    minutes = 0


def set_counter():
    global seconds, miliseconds, minutes, counter_string
    if miliseconds == 9:
        miliseconds = 0
        seconds += 1
    else:
        miliseconds += 1

    if seconds == 60:
        minutes += 1
        seconds = 0

    counter_string = '{:02d}:{:02d}:{}'.format(
        minutes, seconds, miliseconds)


def draw(canvas):
    canvas.draw_text(counter_string, [55, 48], 64, 'white')


# Create frame
frame = simplegui.create_frame("Counter", 300, 200)

frame.set_canvas_background('black')
frame.add_button("Start", start_counter)
frame.add_button("Stop", stop_counter)
frame.add_button("Reset", reset_counter)
timer = simplegui.create_timer(100, set_counter)
frame.set_draw_handler(draw)

# start frame
frame.start()
