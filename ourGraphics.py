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

#Draws snow covered floor
floor = Rectangle(Point(0, 0), Point(winSz, 200))
floor.setFill("white")
floor.draw(NPwin)

#Draws polar bear
##Body
pbBody = Oval(Point(500, 250), Point(800, 100))
pbBody.setFill("azure")
pbBody.draw(NPwin)

#Closes window with user click
NPwin.getMouse()
NPwin.close()
