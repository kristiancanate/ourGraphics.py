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
