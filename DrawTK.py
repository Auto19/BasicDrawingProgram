import tkinter as tk

"""
Left click and Hold to draw
Right Click to toggle between eraser and pen
"""

#Globals are a mess in this code
global color, is_down, x, y # all the variables that are global
is_down = False #start with the pen up
x, y = 0, 0 # X and Y coordinates
color = "black" #start in drawing mode

# Better way to do this (Possible next() command)
def delete(event): #toggle our pen color based on if we are drawing (Black) or erasing (white)
    global color, colors
    if(color == 'black'):
        color = "white"
    elif(color == "white"):
        color = "black"


def write(event): #if our mouse is down, start drawing
    global is_down
    is_down = True

def unwrite(event): #if our mouse is up, stop writing
    global is_down
    is_down = False

def mouse(event): #Basic function that gets the mouse position and sets it to x and y
    global x, y
    x, y = event.x, event.y

def task():
    if(is_down): #If out left click is being held then ->
        canvas.create_rectangle(x, y, x+10, y+10, fill=color, outline=color) #Bigger pen, also possible to use an oval/Circle/etc..
        canvas.postscript(file='image.ps', colormode='color') #Save the image as a ps file (File updates everytime the drawing does)
        #canvas.create_line(x, y, x+1, y+1) #smaller line, bigger gaps when drawing
    root.after(1, task) #Call this to check again at the fastest rate which is 1

root = tk.Tk() #Start our Tk

canvas = tk.Canvas(root, width=400, height=400) # set up canvas typical stuff
canvas.pack()#                                              /\
canvas.old_coords = None #                                  |
canvas.config(background="white") #Set it to white so our eraser which is really a white pen works
canvas.bind('<Motion>', mouse) #Location of the mouse
canvas.bind("<ButtonPress-1>", write) #Left Click down
canvas.bind("<ButtonRelease-1>", unwrite) #Left Click up
canvas.bind("<ButtonPress-3>", delete) #Right click down (We only need to know if its down for toggling)

root.after(1, task)

root.mainloop()