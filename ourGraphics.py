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

#Draws polar bear
##Legs
pbLeg1 = Oval(Point(530, 175), Point(570, 75))
pbLeg1.setFill("azure")
pbLeg1.draw(NPwin)
pbLeg2 = Oval(Point(580, 175), Point(620, 50))
pbLeg2.setFill("azure")
pbLeg2.draw(NPwin)
pbLeg3 = Oval(Point(720, 175), Point(760, 75))
pbLeg3.setFill("azure")
pbLeg3.draw(NPwin)
pbLeg4 = Oval(Point(770, 175), Point(810, 50))
pbLeg4.setFill("azure")
pbLeg4.draw(NPwin)
##Tail
pbTail = Circle(Point(780, 230), 20)
pbTail.setFill("azure")
pbTail.draw(NPwin)
##Body
pbBody = Oval(Point(500, 250), Point(800, 100))
pbBody.setFill("azure")
pbBody.draw(NPwin)
##Ears
pbEar1 = Oval(Point(500, 270), Point(510, 240))
pbEar1.setFill("azure")
pbEar1.draw(NPwin)
pbEar2 = Oval(Point(530, 270), Point(540, 240))
pbEar2.setFill("azure")
pbEar2.draw(NPwin)
##Head
pbHead = Circle(Point(520, 220), 40)
pbHead.setFill("azure")
pbHead.draw(NPwin)
###Nose
pbNose = Oval(Point(510, 220), Point(530, 210))
pbNose.setFill("black")
pbNose.draw(NPwin)
###Eyeballs
pbEB1 = Circle(Point(505, 235), 5)
pbEB1.setFill("white")
pbEB1.draw(NPwin)
pbEB2 = Circle(Point(535, 235), 5)
pbEB2.setFill("white")
pbEB2.draw(NPwin)
####Irises
pbIris1 = Circle(Point(505, 235), 2)
pbIris1.setFill("black")
pbIris1.draw(NPwin)
pbIris2 = Circle(Point(535, 235), 2)
pbIris2.setFill("black")
pbIris2.draw(NPwin)
###Mouth
pbMouth = Oval(Point(505, 200), Point(535, 195))
pbMouth.setFill("pink")
pbMouth.draw(NPwin)

#Closes window with user click
NPwin.getMouse()
NPwin.close()
