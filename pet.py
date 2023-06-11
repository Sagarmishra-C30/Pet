#pet.py - ur cute little pet  - event driven program

from tkinter import HIDDEN, NORMAL, Tk, Canvas  #importing modules from tkinter file
import random
import pygame,os
pygame.init()

#states of the shape drawn -> NORMAL (visible) and HIDDEN (not visible)
# Switching between two states is known as “toggling.”


def toggle_eyes():
    # changing state of eyes of pet
    
    #First the code checks the eyes’ current color: white is open, blue is closed
    current_color = c.itemcget(eye_left, 'fill')
    # This line sets the eyes’ new_color to the opposite value
    new_color = c.body_color if current_color == 'white' else 'white'
    #Now the code checks if the current state of the pupils is NORMAL (visible) or HIDDEN (not visible)
    current_state = c.itemcget(pupil_left, 'state')
    # This line sets the pupils’ new_ state to the opposite value.
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state = new_state)
    c.itemconfigure(pupil_right, state = new_state)
    c.itemconfigure(eye_left, fill = new_color)
    c.itemconfigure(eye_right, fill = new_color)
    
def toggle_left_eye():
    # changing state of only left eye of pet
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state = new_state)
    c.itemconfigure(eye_left, fill = new_color)

    
def blink():
    # makes the eyes blink
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)
    
def wink(event):
    # wink one eye and takes tongue out
    toggle_left_eye()
    toggle_tongue()
    root.after(250, toggle_left_eye)
    root.after(250, toggle_tongue)
    
def show_happy(event):
    # when mouse cursor is moved to pet face , pets become happy
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state = NORMAL)
        c.itemconfigure(cheek_right, state = NORMAL)
        c.itemconfigure(mouth_happy, state = NORMAL)
        c.itemconfigure(mouth_normal, state = HIDDEN)
        c.itemconfigure(mouth_sad, state = HIDDEN)
        return
    
def hide_happy(event):  
    # hides the happy face and comes back to normal when mouse pointer leaves the tkinter window
    c.itemconfigure(cheek_left, state = HIDDEN)
    c.itemconfigure(cheek_right, state = HIDDEN)
    c.itemconfigure(mouth_happy, state = HIDDEN)
    c.itemconfigure(mouth_normal, state = NORMAL)
    c.itemconfigure(mouth_sad, state = HIDDEN)
    c.happy_level = 10
    return

def sad():
    # makes pet sad when ignored for 50 sec
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state = HIDDEN)
        c.itemconfigure(mouth_normal, state = HIDDEN)
        c.itemconfigure(mouth_sad, state = NORMAL)
    else:
        c.happy_level -= 1
        root.after(5000, sad)
        
def toggle_tongue():
    # takes the tongue out 
    if not c.tongue_out:
        c.itemconfigure(tongue_main, state = NORMAL)
        c.itemconfigure(tongue_tip, state = NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_main, state = HIDDEN)
        c.itemconfigure(tongue_tip, state = HIDDEN)
        c.tongue_out  = False

def toggle_pupils():
    # crosses the pupil to the center
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False

def cheeky(event):
    # makes the face cheeky with tongue out
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000, toggle_tongue)
    root.after(1000, toggle_pupils)
    return

def change_color():
    # changes the color of pet every 5 sec
    pet_colors = ['SkyBlue1', 'tomato', 'yellow', 'purple', 'green', 'orange']
    c.body_color = random.choice(pet_colors)
    c.itemconfigure(body, outline = c.body_color, fill = c.body_color)
    c.itemconfigure(ear_left, outline = c.body_color, fill = c.body_color)
    c.itemconfigure(ear_right, outline = c.body_color, fill = c.body_color)
    c.itemconfigure(foot_left, outline = c.body_color, fill = c.body_color)
    c.itemconfigure(foot_right, outline = c.body_color, fill = c.body_color)
    root.after(5000, change_color)
    
root = Tk()                                                                                     # starts Tkinter and open a new window
c = Canvas(root, width = 400, height = 400)                                                      # creates a new canvas obj c with specified attributes
c.configure(bg = 'dark blue', highlightthickness = 0)                                           # configures the canvas obj c with specified attributes

c.body_color = 'SkyBlue1'                                                            # creates new attribute of obj c of class Canvas and set it to 'SkyBlue1'
body = c.create_oval(35, 20, 365, 350, outline = c.body_color, fill = c.body_color ) # create_oval is method of class Canvas, 

# create_polygon is method of class Canvas, first two arg specify the starting point , mid two arg specify middle point, and last two arg specify end points in x-y co-ordinate
# outline is the outline of polygon created and takes color as arg, and fill fills the shape with specified color 
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline = c.body_color, fill = c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline = c.body_color, fill = c.body_color) 

foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill= c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill= c.body_color)

eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')

eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

# These pairs of coordinates define the start, mid-point, and end of the mouth.  The mouth is a smooth line, 2 pixels wide.
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)

tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)


c.pack() #packs canvas into Tkinter window

c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', wink)

c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False 

root.after(1000, blink)
root.after(5000, change_color)
root.after(5000, sad)
# if 'bubbly.bmp' not in os.listdir('newp'):
    # pygame.image.load(c, os.getcwd() + "\\bubbly.bmp")

root.mainloop() 