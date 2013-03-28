from abaqus import *
# this way we have acess to all the abaqus function that we need in general

from abaqusConstants import *
# need this so that the constants like THREE_D and others are working

myModel = mdb.Model(name='Tutorial Model',modelType=STANDARD_EXPLICIT)
myPart = myModel.Part(name='Blech',dimensionality=THREE_D,type=DEFORMABLE_BODY)
mySketch = myModel.ConstrainedSketch(name='Sketch Tutorial', sheetSize=200)
myCoordinates = ((-2.5,-2.5),(-2.5,2.5),(2.5,2.5),(2.5,-2.5))

mySketch.Line(point1=myCoordinates[0],point2=myCoordinates[1])
mySketch.Line(point1 =myCoordinates[1],point2= myCoordinates[2])
mySketch.Line(point1 =myCoordinates[2],point2= myCoordinates[3])
mySketch.Line(point1 =myCoordinates[3],point2= myCoordinates[0])

myPart.BaseSolidExtrude(sketch=mySketch,depth=20)
# this can be done once our sketch is rdy

# first Seed Part
mdb.models['Tutorial Model'] .parts['Blech'].seedPart(size=2)
# assign mesh control
# mesh control only needed if we have to change the default settings
# mesh part command is : myPart.generateMesh() or u use mdb.model['Tutorial Model'].parts['Blech'].generateMesh() 
myPart.generateMesh()
