#ourGraphics by Mariana and Kristian
from graphics import *

#Initializing variables
winSz = 900

#Defining Window
NPwin = GraphWin("North Pole", winSz, winSz)
NPwin.setCoords(0, 0, winSz, winSz)

#Drawing sky background
sky = Rectangle(Point(0, 0), Point(winSz, winSz))
sky.setFill(color_rgb(50, 100, 150))
sky.draw(NPwin)

#Closes window with user click
NPwin.getMouse()
NPwin.close()
