# ******.***************.* **************
# Cantilever Beam bending under the action of a uniform pressure load
# ******.***************.* **************

from abaqus import *
from abaqusConstants import *
import regionToolset

#session.viewports['Viewport: 1'].setValues(displayedObject=None)

# --------------------------------------------------------------------
# Create the model
mdb.models.changeKey(fromName='Model-1', toName='Cantilever Beam')
beamModel = mdb.models['Cantilever Beam']

# --------------------------------------------------------------------
# Create the part

import sketch
import part

# a) Sketch the beam cross section using rectangle tool
beamProfileSketch = beamModel.ConstrainedSketch(name='Beam CS Profile', sheetSize=5)
beamProfileSketch.rectangle(point1=(0.1,0.1), point2=(0.3,-0.1))

# b) Create a 3D deformable part named "Beam" by extruding the sketch
beamPart=beamModel.Part(name='Beam', dimensionality=THREE_D,
type=DEFORMABLE_BODY)
beamPart.BaseSolidExtrude(sketch=beamProfileSketch, depth=5)

# -------------------------------------------------------------
# Create material

import material

# Create material AISI 1005 Steel by assigning mass density, youngs
# modulus and poissons ratio
beamMaterial = beamModel.Material(name='AISI 1005 Steel')
beamMaterial.Density(table=((7872, ), ))
beamMaterial.Elastic(table=((200E9, 0.29), )) 

# Second Page in Book
# ---------------------------------------------------------------
# Create solid section and assign the beam to it

import section

# Create a section to assign to the beam
beamSection = beamModel.HomogeneousSolidSection(name='Beam Section',
							 material='AISI 1005 Steel')

# Assign the beam to this section
beam_region = (beamPart.cells,)
beamPart.SectionAssignment(region=beam_region, sectionName='Beam Section')

# -----------------------------------------------------------------
# Create the assembly
import assembly
# Create the part instance
beamAssembly = beamModel.rootAssembly
beamInstance = beamAssembly.Instance(name='Beam Instance', part=beamPart, dependent=ON)
# -----------------------------------------------------------------
# Create the step

import step
# Create a static general step
beamModel.StaticStep(name='Apply Load', previous='Initial',
				description='Load is applied during this step')
# Create the field output request 
# Change the name of field output request 'F-Output-1' to 'Selected Field Outputs'
beamModel.fieldOutputRequests.changeKey(fromName= 'F-Output-1',
toName='Selected Field Outputs')

# Since F-Output-1 is applied at the 'Apply Load' step by default, 'Selected Field
# Outputs' will be too
# We only need to set the required variables
beamModel.fieldOutputRequests['Selected Field Outputs'].setValues(variables=('S',
'E','PEMAG','U','RF','CF'))
# -----------------------------------------------------------------
# Create the history output request, 

# We try a slightly different method from that used in field output request
#Create a new history output request called 'Default History Outputs' and assign
# both the step and the variables

# Start of Page 3 of Book

beamModel.HistoryOutputRequest(name='Default History Outputs', createStepName='Apply Load', variables=PRESELECT)
# Now delete the original history output request 'H-Output-1'
del beamModel.historyOutputRequests['H-Output-1']
# -----------------------------------------------------------------
# Apply pressure load to top surface

# First we need to locate and select the top surface
# we place a point somewhere on the top surface based on our knowledge of the
# geometry
top_face_pt_x = 0.2
top_face_pt_y = 0.1
top_face_pt_z = 2.5
top_face_pt = (top_face_pt_x,top_face_pt_y,top_face_pt_z)

# The face on which that point lies is the face we are looking for
top_face = beamInstance.faces.findAt((top_face_pt,))

# We extract the region of the face choosing which direction its normal points in
top_face_region=regionToolset.Region(side1Faces=top_face)
# Apply the pressure load on this region in the 'Apply Load' step
beamModel.Pressure(name='Uniform Applied Pressure', createStepName='Apply Load',
					region=top_face_region, distributionType=UNIFORM,
					magnitude=10, amplitude=UNSET)

# -----------------------------------------------------------------
#Apply encastre (fixed) boundary condition to one end to make it cantilever

# First we need to locate and select the top surface
# We place a point somewhere on the top surface based on our knowledge of the
# geometry
fixed_end_face_pt_x = 0.2
fixed_end_face_pt_y = 0
fixed_end_face_pt_z = 0
fixed_end_face_pt = (fixed_end_face_pt_x,fixed_end_face_pt_y,fixed_end_face_pt_z)

# The face on which that point lies is the face we are looking for
fixed_end_face = beamInstance.faces.findAt((fixed_end_face_pt,))
# We  extract the region of the face choosing which direction its normal points in
fixed_end_face_region=regionToolset.Region(faces=fixed_end_face)

beamModel.EncastreBC(name='Encaster one end', createStepName='Initial',
					region=fixed_end_face_region)
# -----------------------------------------------------------------
# Create the mesh

import mesh

#Start of page 4
# First we need to locate and select a point inside the solid
# We place a point somewhere inside it based on our knowledge of the geometry
beam_inside_xcoord=0.2
beam_inside_ycoord=0
beam_inside_zcoord=2.5
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
						kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
						hourglassControl=DEFAULT, distortionControl=DEFAULT)
beamCells=beamPart.cells
selectedBeamCells=beamCells.findAt((beam_inside_xcoord,beam_inside_ycoord,
									beam_inside_zcoord),)
beamMeshRegion=(selectedBeamCells,)
beamPart.setElementType(regions=beamMeshRegion, elemTypes=(elemType1,))

beamPart.seedPart(size=0.1, deviationFactor=0.1)

beamPart.generateMesh()

# -----------------------------------------------------------------
# Create and run the job

import job

# Create the job
mdb.Job(name='CantileverBeamJob', model='Cantilever Beam', type=ANALYSIS,
		explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE,
		description='Job simulates a loaded cantilever beam',
		parallelizationMethodExplicit=DOMAIN, multiprocessingMode=DEFAULT,
		numDomains=1, userSubroutine='', numCpus=1, memory=50,
		memoryUnits=PERCENTAGE, scratch='', echoPrint=OFF, modelPrint=OFF,
		contactPrint=OFF, historyPrint=OFF)
# Run the job 
mdb.jobs['CantileverBeamJob'].submit(consistencyChecking=OFF)

# Do not return control till job is finished running
mdb.jobs['CantileverBeamJob'].waitForCompletion() 

# End of run job
# -----------------------------------------------------------------
# Post processing

import visualization
 
beam_viewport = session.Viewport(name='Beam Results Viewport')
beam_Odb_Path = 'CantileverBeamJob.odb'
an_odb_object = session.openOdb(name=beam_Odb_Path)
beam_viewport.setValues(displayedObject=an_odb_object)

#last page
beam_viewport.odbDisplay.display.setValues(plotState=(DEFORMED,))
