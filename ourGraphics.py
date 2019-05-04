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

def draw_pBear(x, y):
    ##Legs
    draw_oval(x-120, y, x-80, y-100, "azure")
    draw_oval(x-70, y, x-30, y-125, "azure")
    draw_oval(x+70, y, x+110, y-100, "azure")
    draw_oval(x+120, y, x+160, y-125, "azure")
    ##Tail
    draw_cir(x+130, y+55, 20, "azure")
    ##Body
    draw_oval(x-150, y+75, x+150, y-75, "azure")
    ##Ears
    draw_oval(x-150, y+95, x-140, y+65, "azure")
    draw_oval(x-120, y+95, x-110, y+65, "azure")
    ##Head
    draw_cir(x-130, y+45, 40, "azure")
    ###Nose
    draw_oval(x-140, y+45, x-120, y+35, "black")
    ###Eyeballs
    draw_cir(x-145, y+60, 5, "white")
    draw_cir(x-115, y+60, 5, "white")
    ####Irises
    draw_cir(x-145, y+60, 2, "black")
    draw_cir(x-115, y+60, 2, "black")
    ###Mouth
    draw_oval(x-145, y+25, x-115, y+20, "pink")
    
#Defining Window
NPwin = GraphWin("North Pole", winSz, winSz)
NPwin.setCoords(0, 0, winSz, winSz)

#Draws sky, floor and mountains
draw_bckgrnd()

#Draws polar bear
draw_pBear(650, 175)

#Closes window with user click
NPwin.getMouse()
NPwin.close()
