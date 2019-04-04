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

#Drawing Between Mountain
Smallmountain= Polygon(Point(100,200), Point(460,200), Point(260,500))
Smallmountain.setFill(color_rgb(80,100,125))
Smallmountain.draw(NPwin)

#Drawing Between mountain 2
Smallmountain2= Polygon(Point(420,200),Point(970,0), Point(550,500))
Smallmountain2.setFill(color_rgb(80,100,125))
Smallmountain2.draw(NPwin)

#Drawing Mountain
Mountain= Polygon(Point(0,200), Point(350,0), Point(90,550))
Mountain.setFill(color_rgb(60,100,110))
Mountain.draw(NPwin)

#Drawing Mountain 2
Mountain2= Polygon(Point(150,0),Point(600,0),Point(410,550))
Mountain2.setFill(color_rgb(60,100,110))
Mountain2.draw(NPwin)

#Drawing Mountain 3
Mountain3= Polygon(Point(420,0),Point(950,0), Point(750,600))
Mountain3.setFill(color_rgb(60,100,110))
Mountain3.draw(NPwin)

#Draws snow covered floor
floor = Rectangle(Point(0, 0), Point(winSz, 200))
floor.setFill("white")
floor.draw(NPwin)

#Closes window with user click
NPwin.getMouse()
NPwin.close()
