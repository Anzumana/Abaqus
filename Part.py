from abaqus import *
# this way we have acess to all the abaqus function that we need in general
import regionToolset
# need this so that all the region staments work

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

#Apply pressur load to top surface
#First we need to locate and select the top surface
#We place a point somewhere on the top surface based on our knowledge of the geometry

#top_face_pt_x = 2.5 
#top_face_pt_y =	2.5 
#top_face_pt_z = 0 
#top_face_pt = (top_face_pt_x, top_face_pt_y, top_face_pt_z) 


# The face on which that point lies is the face we are looking for
#beamAssembly = beamModel.rootAssembly
#beamInstance = beamAssembly.Instance(name='Beam Instance', part=beamPart,dependent=ON)

#top_face = beamInstance.faces.findAt((top_face_pt,))

# We extract the region of the face choosing which direction its normal points in 

#Apply the pressure load on this region in the 'Apply load' step

