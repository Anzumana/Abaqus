# ******.***************.* **************
# Cantilever Beam bending Under the action of a uniform pressure load
# ******.***************.* **************

from abaqus import *
from abaqusConstants import *
import regionToolset

session.viewports['Viewport: 1'].setValues(displayedObject=None)

# --------------------------------------------------------------------
# Create the model
mdb.models.changeKey(fromName='Model-1', toName='Cantilever Beam')
beamModel = mdb.models['Cantilever Beam']

# --------------------------------------------------------------------
# Create the part

import sketch
import part
# a) Sketch the beam cross section using rectangle tool
beamProfileSketch beamModel.ConstrainedSketch(name-'BeamsheetSize-5) CS Profile',
beamProfileSketch.rectangle(pointl,(0.1,0.1), point2-(0.3,-0.1))
It b) Create a 3D deformable part named "Beam" by extruding the sketch
beamPart-beamModel.Part(name-'Beam', dimensionality-THREE_D,
type-DEFORMABLE_BODV)
beamPart.BaseSolidExtrude(sketch.beamProfileSketch, depth-5)
Create material
mport material
# Create material AISI 1005 Steel by assigning mass density, youngs
it modulus and poissons ratio
beamMaterial = beamModel.Material(name-'AISI 1005 Steel')

# Second Page in Book
======
It
# Create solid section and assign the beam to it
import section
It Create a section to assign to the beam
beamSection = beamModel.HomogeneousSolidSection(name='Beammaterial-'AISI Section', 1005 Steel')
# Assign the beam to this section
Aieam_region (beamPart,cells,)
-mPart.SectionAssignment(region-beam_region, sectionNaMe='Beam Section')
mbly
p r asse ly
Create the part instance
eamAssembly beamModel.rootAssembly
eamInstance = beamAssembly.Instance(name-'Beam Instance' part-beamPart,
dependent=0N)
it Create the step
import step
It Create a static general step
beamModel.StaticStep(name='Apply Load', previous='Initial',
description='Load is applied during this step')
It Create the field output request •
It Change the name of field output request 'F-Output-1' to 'Selected Field Outputs'
beamModel.fieldOutputRequests.changeKey(fromName
toName='Selected Field Outputs')
=
'It Since F-Output-1 is applied at the 'Apply Load' step by default, 'Selected Field
F-Out# Outputs' will be too
It We only need to set the required variables
pbeammodel.fieldOutputRequestsrSelected Field Outputsi.setValues(variables=('S'
'E
ut-1',,
.
It Create the history output request, 
'
ItWe try a slightly different method from that used
P in field output request
ItCreate a new history output request called 'Default History Outputs' and assign
It both the step and the variables
E
M
A

