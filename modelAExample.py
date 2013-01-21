"""
modelAExample.py

A simple example: Creating a part.
"""
# first we import everything we need to use the different abaqus models
from abaqus import *
from abaqusConstants import *
backwardCompatibility.setValues(includeDeprecated=True,
                                reportDeprecated=False)

import sketch
import part

# we create a Model A store that in the model database mdb and we assign this to myModel so we can acess the model very easlily
myModel = mdb.Model(name='Model A')

# we add a Sketch to the model we just created

mySketch = myModel.ConstrainedSketch(name='Sketch A',
                                     sheetSize=200.0)
# now we define the outer coordinates for our sketch is supposed to become a 3 dimentional A
# imporant so see that we have to add the first point a second time at the end of our array of points
# this is dude to the algorithm with which we draw the lines. this is the only way so that we don't get any exeptions for accessing the array
# and also so that we can draw all the necessary lines 
xyCoordsInner = ((-5 , 20), (5, 20), (15, 0),
    (-15, 0), (-5, 20))

xyCoordsOuter = ((-10, 30), (10, 30), (40, -30),
    (30, -30), (20, -10), (-20, -10),
    (-30, -30), (-40, -30), (-10, 30))

# the following 2 loops draw lines between all of the differnt points previously defined

for i in range(len(xyCoordsInner)-1):
    mySketch.Line(point1=xyCoordsInner[i],
        point2=xyCoordsInner[i+1])

for i in range(len(xyCoordsOuter)-1):
    mySketch.Line(point1=xyCoordsOuter[i],
        point2=xyCoordsOuter[i+1])

# creates a deformable part and add this part to our model
myPart = myModel.Part(name='Part A', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
# now we have a 2 dimentional drawing of a and now we give it a depth of 20 to make it 3d
myPart.BaseSolidExtrude(sketch=mySketch, depth=20.0)
# create a view port in the gui so that we can take a look at what we created internaly
myViewport = session.Viewport(name='Viewport for Model A',
    origin=(10, 10), width=150, height=100)

myViewport.setValues(displayedObject=myPart)

myViewport.partDisplay.setValues(renderStyle=SHADED)
