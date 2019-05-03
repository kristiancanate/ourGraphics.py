#ourGraphics by Mariana and Kristian
from graphics import *

#Initializing variables
winSz = 900
gray = color_rgb(80, 100, 125)
green = color_rgb(60, 100, 110)
blue = color_rgb(50, 100, 150)

def draw_poly(x1, y1, x2, y2, x3, y3, col):
    poly = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    poly.setFill(col)
    poly.draw(NPwin)

def draw_rec(x1, y1, x2, y2, col):
    rec = Rectangle(Point(x1, y1), Point(x2, y2))
    rec.setFill(col)
    rec.draw(NPwin)

def draw_oval(x1, y1, x2, y2, col):
    oval = Oval(Point(x1, y1), Point(x2, y2))
    oval.setFill(col)
    oval.draw(NPwin)

def draw_cir(x, y, rad, col):
    pbTail = Circle(Point(x, y), rad)
    pbTail.setFill(col)
    pbTail.draw(NPwin)

def draw_sky():
    draw_rec(0, 0, winSz, winSz, blue)

def draw_floor():
    draw_rec(0, 0, winSz, 200, "white")

def draw_mntn():
    draw_poly(100, 200, 460, 200, 260, 500, gray) #Drawing Between Mountain
    draw_poly(420, 200, 970, 0, 550, 500, gray) #Drawing Between mountain 2
    draw_poly(0, 200, 350, 0, 90, 550, green) #Drawing Mountain
    draw_poly(150, 0, 600, 0, 410, 550, green) #Drawing Mountain 2
    draw_poly(420, 0, 950, 0, 750, 600, green) #Drawing Mountain 3

def draw_bckgrnd():
    draw_sky()
    draw_mntn()
    draw_floor()

#Defining Window
NPwin = GraphWin("North Pole", winSz, winSz)
NPwin.setCoords(0, 0, winSz, winSz)

#Draws sky, floor and mountains
draw_bckgrnd()

#Draws polar bear
##Legs
draw_oval(530, 175, 570, 75, "azure")
draw_oval(580, 175, 620, 50, "azure")
draw_oval(720, 175, 760, 75, "azure")
draw_oval(770, 175, 810, 50, "azure")
##Tail
draw_cir(780, 230, 20, "azure")
##Body
draw_oval(500, 250, 800, 100, "azure")
##Ears
draw_oval(500, 270, 510, 240, "azure")
draw_oval(530, 270, 540, 240, "azure")
##Head
draw_cir(520, 220, 40, "azure")
###Nose
draw_oval(510, 220, 530, 210, "black")
###Eyeballs
draw_cir(505, 235, 5, "white")
draw_cir(535, 235, 5, "white")
####Irises
draw_cir(505, 235, 2, "black")
draw_cir(535, 235, 2, "black")
###Mouth
draw_oval(505, 200, 535, 195, "pink")

#Closes window with user click
NPwin.getMouse()
NPwin.close()
