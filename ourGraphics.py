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

#Drawing Mountain
Mountain= Polygon(Point(0,200), Point(350,0), Point(150,600))
Mountain.setFill(color_rgb(60,130,100))
Mountain.draw(NPwin)

#Drawing Mountain 2
Mountain2= Polygon(Point(340,0),Point(560,0),Point(430,550))
Mountain2.setFill(color_rgb(60,130,100))
Mountain2.draw(NPwin)

#Draws snow covered floor
floor = Rectangle(Point(0, 0), Point(winSz, 200))
floor.setFill("white")
floor.draw(NPwin)

#Closes window with user click
NPwin.getMouse()
NPwin.close()
