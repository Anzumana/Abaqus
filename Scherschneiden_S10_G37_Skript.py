# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

#-----------------------------------------------------------------------
#Definition der Geometrieparameter
#-----------------------------------------------------------------------
rst=0.01        # Schneidkantenradius des Stempels
rm=0.01         # Schneidkantenradius der Matrize
rnh=0.1         # Kantenradius des Niederhalters
rb=24.0         # Blechlänge
d=1.4           # Blechdecke
A=0.01          # Abstand Stempel - Oberseite Blech
D=10.0          # Stempelradius
A1=0.0          # Abstand Niederhalter - Oberseite Blech
F=10.45         # Innenradius Niederhalter
I=25.0          # Außenradius Niederhalter und Matrize
L=10.15         # Innenradius Matrize
N=0.0           # Abstand Matrize - Unterseite Blech
B=d+A            
B1=d+A1         
C=B+rst          
E=D-rst
G=F+rnh
H=B1+rnh
K=B+4.0
M=L+rm
O=N+rm
P=N+4
RF1X=5.0        # x-Koordinate Reference Point des Stempels
RF1Y=3.0        # y-Koordinate Reference Point des Stempels
RF2X=15.0       # x-Koordinate Reference Point des Niderhalters
RF2Y=3.0        # y-Koordinate Reference Point des Niderhalters
RF3X=15.0       # x-Koordinate Reference Point der Matrize
RF3Y=-2.0       # y-Koordinate Reference Point der Matrize



#-----------------------------------------------------------------------
#Definition der Partitionsparameter
#-----------------------------------------------------------------------
P1=9.595
P2=9.63
P3=9.6825
P4=9.7
P5=10.4525
P6=10.47
P7=10.5225
P8=10.5575

#-----------------------------------------------------------------------
#Definition der Materialparameter
#-----------------------------------------------------------------------
JCA=490.0       # Johnson-Cook Parameter A
JCB=885.8       # Johnson-Cook Parameter B
JCn=0.3036      # Johnson-Cook Parameter n
JCC=0.0286      # Johnson-Cook Parameter C
JCm=1000000.0   # Johnson-Cook Parameter m
JCMT=1520.0     # Johnson-Cook Parameter Tm
JCTT=20.0       # Johnson-Cook Parameter Tr
d1=0.2888       # Johnson-Cook Parameter d1
d2=0.4648       # Johnson-Cook Parameter d2
d3=2.925        # Johnson-Cook Parameter d3
d4=0.002        # Johnson-Cook Parameter d4
d5=7.5          # Johnson-Cook Parameter d5
epsdotzero=1.0  # Johnson-Cook Parameter epsilon dot zero
de=0.000175     # Damage Evolution
cp=477000000.0  # späzifische W#ärmekapazität

#-----------------------------------------------------------------------
#Definition der Niederhaltekraft als Parameter
#-----------------------------------------------------------------------
f=-200000.0

#-----------------------------------------------------------------------
#Definition der Massenskalierungsfaktoren als Parameter
#-----------------------------------------------------------------------
ms1=100.0       # Massenskallierungsfaktor im Schritt "Einspannung" 
ms2=100.0       # Massenskallierungsfaktor im Schritt "Schneidvorgang"

#-----------------------------------------------------------------------
#Definition der Schrittzeit als Parameter
#-----------------------------------------------------------------------
t1=0.002        # Dauer des Schrittes "Einspannung"
t2=0.0192       # Dauer des Schrittes "Schneidvorgang"

#-----------------------------------------------------------------------
#Definition der Schneidtiefe als Parameter
#-----------------------------------------------------------------------
ts=0.71

#-----------------------------------------------------------------------
#Anzahl der Elemente entlang der Kanten als parameter
#-----------------------------------------------------------------------
s1=137
s2=1
s3=3
s4=1
s5=86
s6=192
s7=40
s8=80
s9=160

#-----------------------------------------------------------------------
#Erzeugung der Geometrie
#-----------------------------------------------------------------------
Model=mdb.models['Model-1']

Model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
Model.sketches['__profile__'].sketchOptions.setValues(viewStyle=AXISYM)
Model.sketches['__profile__'].ConstructionLine(point1=(0.0, -100.0), 
	point2=(0.0, 100.0))
Model.sketches['__profile__'].FixedConstraint(entity=
    Model.sketches['__profile__'].geometry[2])
Model.sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(rb, 0.0))
Model.sketches['__profile__'].HorizontalConstraint(entity=
    Model.sketches['__profile__'].geometry[3])
Model.sketches['__profile__'].Line(point1=(rb, 0.0), point2=(rb, d))
Model.sketches['__profile__'].VerticalConstraint(entity=
    Model.sketches['__profile__'].geometry[4])
Model.sketches['__profile__'].PerpendicularConstraint(entity1=
    Model.sketches['__profile__'].geometry[3], entity2=
    Model.sketches['__profile__'].geometry[4])
Model.sketches['__profile__'].Line(point1=(rb, d), point2=(0.0, d))
Model.sketches['__profile__'].HorizontalConstraint(entity=
    Model.sketches['__profile__'].geometry[5])
Model.sketches['__profile__'].PerpendicularConstraint(entity1=
    Model.sketches['__profile__'].geometry[4], entity2=
    Model.sketches['__profile__'].geometry[5])
Model.sketches['__profile__'].Line(point1=(0.0, d), point2=(0.0, 0.0))
Model.sketches['__profile__'].VerticalConstraint(entity=
    Model.sketches['__profile__'].geometry[6])
	
Model.sketches['__profile__'].PerpendicularConstraint(entity1=
    Model.sketches['__profile__'].geometry[5], entity2=
    Model.sketches['__profile__'].geometry[6])
Model.Part(dimensionality=AXISYMMETRIC, name='Blech', type=
    DEFORMABLE_BODY)
Model.parts['Blech'].BaseShell(sketch=
    Model.sketches['__profile__'])
del Model.sketches['__profile__']

Model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
Model.sketches['__profile__'].sketchOptions.setValues(viewStyle=AXISYM)
Model.sketches['__profile__'].ConstructionLine(point1=(0.0, -100.0), 
	point2=(0.0, 100.0))
Model.sketches['__profile__'].FixedConstraint(entity=
    Model.sketches['__profile__'].geometry[2])
Model.sketches['__profile__'].Line(point1=(0.0, B), point2=(E, B))
Model.sketches['__profile__'].HorizontalConstraint(entity=
    Model.sketches['__profile__'].geometry[3])
Model.sketches['__profile__'].Line(point1=(D, C), point2=(D, K))
Model.sketches['__profile__'].VerticalConstraint(entity=
    Model.sketches['__profile__'].geometry[4])
Model.sketches['__profile__'].ArcByCenterEnds(center=(E, C),
    direction=CLOCKWISE, point1=(D, C), point2=(E, B))
Model.Part(dimensionality=AXISYMMETRIC, name='Stempel', type=
    ANALYTIC_RIGID_SURFACE)
Model.parts['Stempel'].AnalyticRigidSurf2DPlanar(sketch=
    Model.sketches['__profile__'])
del Model.sketches['__profile__']

Model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
Model.sketches['__profile__'].sketchOptions.setValues(viewStyle=AXISYM)
Model.sketches['__profile__'].ConstructionLine(point1=(0.0, -100.0), 
	point2=(0.0, 100.0))
Model.sketches['__profile__'].FixedConstraint(entity=
    Model.sketches['__profile__'].geometry[2])
Model.sketches['__profile__'].Line(point1=(F, K), point2=(F, H))
Model.sketches['__profile__'].VerticalConstraint(entity=
    Model.sketches['__profile__'].geometry[3])
Model.sketches['__profile__'].Line(point1=(G, B1), point2=(I, B1))
Model.sketches['__profile__'].HorizontalConstraint(entity=
    Model.sketches['__profile__'].geometry[4])
Model.sketches['__profile__'].ArcByCenterEnds(center=(G, H), 
	direction=CLOCKWISE, point1=(G, B1), point2=(F, H))
Model.Part(dimensionality=AXISYMMETRIC, name='Niederhalter', type=
    ANALYTIC_RIGID_SURFACE)
Model.parts['Niederhalter'].AnalyticRigidSurf2DPlanar(sketch=
    Model.sketches['__profile__'])
del Model.sketches['__profile__']
Model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
Model.sketches['__profile__'].sketchOptions.setValues(viewStyle=AXISYM)
Model.sketches['__profile__'].ConstructionLine(point1=(0.0, -100.0), 
	point2=(0.0, 100.0))
Model.sketches['__profile__'].FixedConstraint(entity=
    Model.sketches['__profile__'].geometry[2])
Model.sketches['__profile__'].Line(point1=(L, -P), point2=(L, -O))
Model.sketches['__profile__'].VerticalConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
Model.sketches['__profile__'].Line(point1=(M, -N), point2=(I, -N))
Model.sketches['__profile__'].HorizontalConstraint(entity=
    Model.sketches['__profile__'].geometry[4])
Model.sketches['__profile__'].ArcByCenterEnds(center=(M, -O), 
	direction=CLOCKWISE, point1=(L, -O), point2=(M, -N))
Model.Part(dimensionality=AXISYMMETRIC, name='Matrize', type=
    ANALYTIC_RIGID_SURFACE)
Model.parts['Matrize'].AnalyticRigidSurf2DPlanar(sketch=
    Model.sketches['__profile__'])
del Model.sketches['__profile__']

#-----------------------------------------------------------------------
#Definition der Materialeigenschaften
#-----------------------------------------------------------------------
Model.Material(name='HCT780XD')
Model.materials['HCT780XD'].Density(table=((7.86e-09, ), ))
Model.materials['HCT780XD'].Elastic(table=((237000.0, 0.3), ))
Model.materials['HCT780XD'].Plastic(hardening=JOHNSON_COOK, 
    table=((JCA, JCB, JCn, JCm, JCMT, JCTT), ))
Model.materials['HCT780XD'].JohnsonCookDamageInitiation(table=(
	(d1, d2, d3, d4, d5, JCMT, JCTT, epsdotzero), ))
Model.materials['HCT780XD'].johnsonCookDamageInitiation.DamageEvolution(
    table=((de, ), ), type=DISPLACEMENT)
Model.materials['HCT780XD'].InelasticHeatFraction()
Model.materials['HCT780XD'].SpecificHeat(table=((477000000.0, ), ))
Model.materials['HCT780XD'].plastic.RateDependent(table=((0.0286, 
	epsdotzero), ), type=JOHNSON_COOK)

#-----------------------------------------------------------------------
#Definition von "Section"
#-----------------------------------------------------------------------
Model.HomogeneousSolidSection(material='HCT780XD', name='Section-1', 
	thickness=1.0)

#-----------------------------------------------------------------------
#Definition von "Reference Point" beim Stempel
#-----------------------------------------------------------------------
Model.parts['Stempel'].ReferencePoint(point=(RF1X, RF1Y, 0.0))

#-----------------------------------------------------------------------
#Definition von "Reference Point" beim Niederhalter
#-----------------------------------------------------------------------
Model.parts['Niederhalter'].ReferencePoint(point=(RF2X, RF2Y, 0.0))

#-----------------------------------------------------------------------
#Definition von "Reference Point" bei der Matrize
#-----------------------------------------------------------------------
Model.parts['Matrize'].ReferencePoint(point=(RF3X, RF3Y, 0.0))

#-----------------------------------------------------------------------
#Definition von "Sets" beim Stempel
#-----------------------------------------------------------------------
Model.parts['Stempel'].Set(name='Set-RF-Stempel', referencePoints=(
	Model.parts['Stempel'].referencePoints[2], ))
	
#-----------------------------------------------------------------------
#Definition von "Sets" beim Niederhalter
#-----------------------------------------------------------------------
Model.parts['Niederhalter'].Set(name='Set-RF-Niederhalter', 
    referencePoints=( Model.parts['Niederhalter'].referencePoints[2], ))
	
#-----------------------------------------------------------------------
#Definition von "Sets" bei der Matrize
#-----------------------------------------------------------------------
Model.parts['Matrize'].Set(name='Set-RF-Matrize', referencePoints=(
	Model.parts['Matrize'].referencePoints[2], ))

#-----------------------------------------------------------------------
#Definition von "Sets" beim Blech
#-----------------------------------------------------------------------
Model.parts['Blech'].Set(faces=
	Model.parts['Blech'].faces.getSequenceFromMask(('[#1 ]', ), ), 
	name='Set-Blech')
Model.parts['Blech'].Set(edges=
    Model.parts['Blech'].edges.getSequenceFromMask(('[#1 ]', ), ), 
	name='Set-linke Kante')
Model.parts['Blech'].Set(edges=
    Model.parts['Blech'].edges.getSequenceFromMask(('[#4 ]', ), ), 
	name='Set-Festlager rechts')

#-----------------------------------------------------------------------
#Definition der Oberfläche des Stempels
#-----------------------------------------------------------------------
Model.parts['Stempel'].Surface(name='Surf-Oberfläche Stempel', 
	side2Edges=Model.parts['Stempel'].edges.getSequenceFromMask((
	'[#1 ]', ), ))

#-----------------------------------------------------------------------
#Definition der Oberfläche des Niederhalters
#-----------------------------------------------------------------------
Model.parts['Niederhalter'].Surface(name='Surf-Oberfläche Niederhalter', 
	side2Edges=Model.parts['Niederhalter'].edges.getSequenceFromMask((
	'[#1 ]', ), ))

#-----------------------------------------------------------------------
#Definition der Oberfläche der Matrize
#-----------------------------------------------------------------------
Model.parts['Matrize'].Surface(name='Surf-Oberfläche Matrize', 
	side1Edges=Model.parts['Matrize'].edges.getSequenceFromMask((
	'[#1 ]', ), ))

#-----------------------------------------------------------------------
#Definition der Oberflächen des Blechs
#-----------------------------------------------------------------------
Model.parts['Blech'].Surface(name='Surf-obere Oberfläche', 
    side1Edges=Model.parts['Blech'].edges.getSequenceFromMask((
    '[#8 ]', ), ))
Model.parts['Blech'].Surface(name='Surf-untere Oberfläche', 
    side1Edges=Model.parts['Blech'].edges.getSequenceFromMask((
    '[#2 ]', ), ))

#-----------------------------------------------------------------------
#Definition von "Datumpoints" beim Blech
#-----------------------------------------------------------------------
Model.parts['Blech'].DatumPointByCoordinate(coords=(P1, 0.0, 0.0))
Model.parts['Blech'].DatumPointByCoordinate(coords=(P2, 0.0, 0.0))
Model.parts['Blech'].DatumPointByCoordinate(coords=(P3, 0.0, 0.0))
Model.parts['Blech'].DatumPointByCoordinate(coords=(P4, 0.0, 0.0))
Model.parts['Blech'].DatumPointByCoordinate(coords=(P5, 0.0, 0.0))
Model.parts['Blech'].DatumPointByCoordinate(coords=(P6, 0.0, 0.0))
Model.parts['Blech'].DatumPointByCoordinate(coords=(P7, 0.0, 0.0))
Model.parts['Blech'].DatumPointByCoordinate(coords=(P8, 0.0, 0.0))

#-----------------------------------------------------------------------
#Definition von "Datumplane" beim Blech
#-----------------------------------------------------------------------
Model.parts['Blech'].DatumPlaneByPointNormal(normal=Model.parts[
	'Blech'].edges[1], point=Model.parts['Blech'].datums[7])
Model.parts['Blech'].DatumPlaneByPointNormal(normal=Model.parts[
	'Blech'].edges[1], point=Model.parts['Blech'].datums[8])
Model.parts['Blech'].DatumPlaneByPointNormal(normal=Model.parts[
	'Blech'].edges[1], point=Model.parts['Blech'].datums[9])
Model.parts['Blech'].DatumPlaneByPointNormal(normal=Model.parts[
	'Blech'].edges[1], point=Model.parts['Blech'].datums[10])
	
Model.parts['Blech'].DatumPlaneByPointNormal(normal=Model.parts[
	'Blech'].edges[1], point=Model.parts['Blech'].datums[11])
Model.parts['Blech'].DatumPlaneByPointNormal(normal=Model.parts[
	'Blech'].edges[1], point=Model.parts['Blech'].datums[12])
Model.parts['Blech'].DatumPlaneByPointNormal(normal=Model.parts[
	'Blech'].edges[1], point=Model.parts['Blech'].datums[13])
Model.parts['Blech'].DatumPlaneByPointNormal(normal=Model.parts[
	'Blech'].edges[1], point=Model.parts['Blech'].datums[14])

#-----------------------------------------------------------------------
#Definition der Partitionen beim Blech
#-----------------------------------------------------------------------
Model.parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
    Model.parts['Blech'].datums[15], faces=Model.parts[
	'Blech'].faces.getSequenceFromMask(('[#1 ]', ), ))
Model.parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
	Model.parts['Blech'].datums[16], faces=Model.parts[
	'Blech'].faces.getSequenceFromMask(('[#2 ]', ), ))
Model.parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
    Model.parts['Blech'].datums[17], faces=Model.parts[
	'Blech'].faces.getSequenceFromMask(('[#4 ]', ), ))
	
Model.parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
    Model.parts['Blech'].datums[18], faces=Model.parts[
	'Blech'].faces.getSequenceFromMask(('[#8 ]', ), ))
Model.parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
    Model.parts['Blech'].datums[19], faces=Model.parts[
	'Blech'].faces.getSequenceFromMask(('[#10 ]', ), ))
Model.parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
    Model.parts['Blech'].datums[20], faces=Model.parts[
	'Blech'].faces.getSequenceFromMask(('[#20 ]', ), ))
Model.parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
    Model.parts['Blech'].datums[21], faces=Model.parts[
	'Blech'].faces.getSequenceFromMask(('[#40 ]', ), ))
Model.parts['Blech'].PartitionFaceByDatumPlane(datumPlane=
    Model.parts['Blech'].datums[22], faces=Model.parts[
	'Blech'].faces.getSequenceFromMask(('[#80 ]', ), ))

#-----------------------------------------------------------------------
#Definition von "Sets" beim Blech für ALE
#-----------------------------------------------------------------------
Model.parts['Blech'].Set(faces=
	Model.parts['Blech'].faces.getSequenceFromMask(('[#8 ]', ), ), 
	name='Set-ALE_Bereich')

	
	
	
#-----------------------------------------------------------------------
#Kreierung von "Assembly"
#-----------------------------------------------------------------------
Model.rootAssembly.DatumCsysByThreePoints(coordSysType=
    CYLINDRICAL, origin=(0.0, 0.0, 0.0), point1=(1.0, 0.0, 0.0), 
	point2=(0.0, 0.0, -1.0))
Model.rootAssembly.Instance(dependent=OFF, name='Blech-1', part=
	Model.parts['Blech'])
Model.rootAssembly.Instance(dependent=OFF, name='Stempel-1', part=
	Model.parts['Stempel'])
Model.rootAssembly.Instance(dependent=OFF, name='Niederhalter-1', part=
	Model.parts['Niederhalter'])
Model.rootAssembly.Instance(dependent=OFF, name='Matrize-1', part=
	Model.parts['Matrize'])

#-----------------------------------------------------------------------
#Definition von "Constraints" für den Stempel
#-----------------------------------------------------------------------
Model.RigidBody(name='Constraint-Stempel', refPointRegion=
    Model.rootAssembly.instances['Stempel-1'].sets['Set-RF-Stempel'], 
	surfaceRegion=Model.rootAssembly.instances['Stempel-1'].surfaces[
	'Surf-Oberfläche Stempel'])
	
#-----------------------------------------------------------------------
#Definition von "Constraints" für den Niederhalter
#-----------------------------------------------------------------------
Model.RigidBody(name='Constraint-Niederhalter', refPointRegion=
    Model.rootAssembly.instances['Niederhalter-1'].sets[
	'Set-RF-Niederhalter'], surfaceRegion=Model.rootAssembly.instances[
	'Niederhalter-1'].surfaces['Surf-Oberfläche Niederhalter'])

#-----------------------------------------------------------------------
#Definition von "Constraints" für die Matrize
#-----------------------------------------------------------------------
Model.RigidBody(name='Constraint-Matrize', refPointRegion=
    Model.rootAssembly.instances['Matrize-1'].sets['Set-RF-Matrize'], 
	surfaceRegion=Model.rootAssembly.instances['Matrize-1'].surfaces[
	'Surf-Oberfläche Matrize'])

#-----------------------------------------------------------------------
#Definition von "Inertias" für den Stempel, den Niederhalter und Matrize
#-----------------------------------------------------------------------
Model.rootAssembly.engineeringFeatures.PointMassInertia(alpha=0.0, 
	composite=0.0, mass=0.0001, name='Inertia-Stempel', region=
    Model.rootAssembly.instances['Stempel-1'].sets['Set-RF-Stempel'])
	
	
	
Model.rootAssembly.engineeringFeatures.PointMassInertia(alpha=0.0, 
	composite=0.0, mass=0.0001, name='Inertia-Niederhalter', region=
    Model.rootAssembly.instances['Niederhalter-1'].sets[
	'Set-RF-Niederhalter'])
Model.rootAssembly.engineeringFeatures.PointMassInertia(alpha=0.0, 
	composite=0.0, mass=0.0001, name='Inertia-Matrize', region=
    Model.rootAssembly.instances['Matrize-1'].sets['Set-RF-Matrize'])
	
#-----------------------------------------------------------------------
#Definition von "Steps"
#-----------------------------------------------------------------------
Model.ExplicitDynamicsStep(massScaling=((SEMI_AUTOMATIC, 
    Model.rootAssembly.instances['Blech-1'].sets['Set-Blech'], 
    AT_BEGINNING, ms1, 0.0, None, 0, 0, 0.0, 0.0, 0, None), ), name=
    'Einspannung', previous='Initial', timePeriod=t1)
Model.ExplicitDynamicsStep(massScaling=((SEMI_AUTOMATIC, 
    Model.rootAssembly.instances['Blech-1'].sets['Set-Blech'], 
    AT_BEGINNING, ms2, 0.0, None, 0, 0, 0.0, 0.0, 0, None), ), name=
    'Schneidvorgang', previous='Einspannung', timePeriod=t2)	
Model.steps['Schneidvorgang'].setValues(adiabatic=ON, 
    massScaling=((SEMI_AUTOMATIC, Model.rootAssembly.instances[
	'Blech-1'].sets['Set-Blech'], AT_BEGINNING, 100.0, 0.0, None, 
	0, 0, 0.0, 0.0, 0, None), ))

#-----------------------------------------------------------------------
#Definition von "History Output" am "Reference Point" des Stempels
#-----------------------------------------------------------------------
Model.HistoryOutputRequest(createStepName='Einspannung', name=
    'H-Output-RP-Stempel', rebar=EXCLUDE, region=Model.rootAssembly.
	instances['Stempel-1'].sets['Set-RF-Stempel'], sectionPoints=
	DEFAULT, variables=('U2', 'RF2'))
	
#-----------------------------------------------------------------------
#Definition von "History Output" am "Reference point" des Niederhalters
#-----------------------------------------------------------------------
Model.HistoryOutputRequest(createStepName='Einspannung', name=
    'H-Output-RP-Niederhalter', rebar=EXCLUDE, region=Model.rootAssembly.
	instances['Niederhalter-1'].sets['Set-RF-Niederhalter'], 
	sectionPoints=DEFAULT, variables=('U2', 'RF2'))

#-----------------------------------------------------------------------
#Definition von "Field Output"
#-----------------------------------------------------------------------
Model.fieldOutputRequests['F-Output-1'].setValues(numIntervals=50, 
	variables=('S', 'SVAVG', 'TRIAX', 'E', 'PE', 'PEVAVG', 'PEEQ', 
    'PEEQVAVG', 'LE', 'U', 'V', 'A', 'RF', 'CSTRESS', 'CFAILURE', 
	'EVF', 'DMICRT', 'TEMP', 'STATUS'))

#-----------------------------------------------------------------------
#Amplitude für den Schritt "Einspannung"
#-----------------------------------------------------------------------
Model.SmoothStepAmplitude(data=((0.0, 0.0), (t1, 1.0)), name=
	'Amp-Einspannung', timeSpan=STEP)

#-----------------------------------------------------------------------
#Amplitude für den Schritt "Schneidvorgang"
#-----------------------------------------------------------------------
Model.TabularAmplitude(data=((0.0, 0.0), (t2, 1.0)), name=
    'Amp-Schneidvorgang', smooth=SOLVER_DEFAULT, timeSpan=STEP)

#-----------------------------------------------------------------------
#Aufbringung der Niederhalterkraft
#-----------------------------------------------------------------------
Model.ConcentratedForce(amplitude='Amp-Einspannung', cf2=f, 
	createStepName='Einspannung', distributionType=UNIFORM, field='', 
	localCsys=None, name='Load-Niederhalter', region=Model.rootAssembly.
	instances['Niederhalter-1'].sets['Set-RF-Niederhalter'])

#-----------------------------------------------------------------------
#Definition der Randbedingungen	
#-----------------------------------------------------------------------
Model.DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
	'BC-Matrize', region=Model.rootAssembly.instances['Matrize-1'].
	sets['Set-RF-Matrize'], u1=SET, u2=SET, ur3=SET)
Model.DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
	'BC-Stempel', region=Model.rootAssembly.instances['Stempel-1'].
	sets['Set-RF-Stempel'], u1=SET, u2=SET, ur3=SET)
Model.DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
    'BC-linke Kante', region=Model.rootAssembly.instances['Blech-1'].
	sets['Set-linke Kante'], u1=SET, u2=UNSET, ur3=SET)
Model.DisplacementBC(amplitude=UNSET, createStepName='Schneidvorgang', 
	distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, 
	name='BC-Festlager rechts', region=Model.rootAssembly.instances[
	'Blech-1'].sets['Set-Festlager rechts'], u1=0.0, u2=UNSET, ur3=0.0)
Model.DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
    'BC-Niederhalter', region=Model.rootAssembly.instances[
	'Niederhalter-1'].sets['Set-RF-Niederhalter'], u1=SET, u2=UNSET, 
	ur3=SET)
Model.boundaryConditions['BC-Stempel'].setValuesInStep(amplitude=
	'Amp-Schneidvorgang', stepName='Schneidvorgang', u2=-ts)
	
	
#-----------------------------------------------------------------------
#Definition von "Section Assiggnements"
#-----------------------------------------------------------------------
Model.parts['Blech'].SectionAssignment(offset=0.0, offsetField='', 
	offsetType=MIDDLE_SURFACE, region=Model.parts['Blech'].sets[
	'Set-Blech'], sectionName='Section-1')
Model.rootAssembly.regenerate()

#-----------------------------------------------------------------------
#Erzeugen von "seed"
#-----------------------------------------------------------------------
Model.rootAssembly.seedEdgeByNumber(edges=Model.rootAssembly.instances[
	'Blech-1'].edges.getSequenceFromMask(('[#1400000 ]', ), ), number=s1)
Model.rootAssembly.seedEdgeByNumber(edges=Model.rootAssembly.instances[
	'Blech-1'].edges.getSequenceFromMask(('[#28000a ]', ), ), number=s2)
Model.rootAssembly.seedEdgeByNumber(edges=Model.rootAssembly.instances[
	'Blech-1'].edges.getSequenceFromMask(('[#50050 ]', ), ), number=s3)
Model.rootAssembly.seedEdgeByNumber(edges=Model.rootAssembly.instances[
	'Blech-1'].edges.getSequenceFromMask(('[#a280 ]', ), ), number=s4)
Model.rootAssembly.seedEdgeByNumber(edges=Model.rootAssembly.instances[
	'Blech-1'].edges.getSequenceFromMask(('[#1400 ]', ), ), number=s5)
Model.rootAssembly.seedEdgeByNumber(edges=Model.rootAssembly.instances[
	'Blech-1'].edges.getSequenceFromMask(('[#a000000 ]', ), ), number=s6)
Model.rootAssembly.seedEdgeByNumber(edges=Model.rootAssembly.instances[
	'Blech-1'].edges.getSequenceFromMask(('[#4800000 ]', ), ), number=s7)
Model.rootAssembly.seedEdgeByNumber(edges=Model.rootAssembly.instances[
	'Blech-1'].edges.getSequenceFromMask(('[#120005 ]', ), ), number=s8)
Model.rootAssembly.seedEdgeByNumber(edges=Model.rootAssembly.instances[
	'Blech-1'].edges.getSequenceFromMask(('[#4920 ]', ), ), number=s9)

#-----------------------------------------------------------------------
#Assignation von "Mesh Controls"
#-----------------------------------------------------------------------
Model.rootAssembly.setMeshControls(regions=Model.rootAssembly.instances[
	'Blech-1'].faces.getSequenceFromMask(('[#1aa ]', ), ), technique=
	STRUCTURED)
Model.rootAssembly.setMeshControls(elemShape=TRI, regions=
    Model.rootAssembly.instances['Blech-1'].faces.getSequenceFromMask(
    ('[#55 ]', ), ), technique=STRUCTURED)
	
#-----------------------------------------------------------------------
#Assignation von "Element Type"
#-----------------------------------------------------------------------
Model.rootAssembly.setElementType(elemTypes=(ElemType(elemCode=CAX4R, 
	elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, hourglassControl=
	DEFAULT, distortionControl=DEFAULT), ElemType(elemCode=CAX3, 
	elemLibrary=EXPLICIT)), regions=(Model.rootAssembly.instances[
	'Blech-1'].faces.getSequenceFromMask(('[#1aa ]', ), ), ))
#-----------------------------------------------------------------------
#Definition von "Interaction Properties"
#-----------------------------------------------------------------------
Model.ContactProperty('Reibung')
Model.interactionProperties['Reibung'].NormalBehavior(allowSeparation=
	ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
Model.interactionProperties['Reibung'].TangentialBehavior(dependencies=
	0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=
	PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressure
	Dependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.1, ), ), temperatureDependency=OFF)
Model.ContactProperty('Keine Reibung')
Model.interactionProperties['Keine Reibung'].NormalBehavior(allow
	Separation=ON, constraintEnforcementMethod=DEFAULT, pressure
	Overclosure=HARD)
Model.interactionProperties['Keine Reibung'].TangentialBehavior(
    formulation=FRICTIONLESS)
Model.interactionProperties['Reibung'].tangentialBehavior.setValues(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=290.0, slipRateDependency=
	OFF, table=((0.1, ), ), temperatureDependency=OFF)
Model.interactionProperties['Reibung'].normalBehavior.setValues(
    constraintEnforcementMethod=DEFAULT, maxStiffness=10000000.0, 
    pressureOverclosure=EXPONENTIAL, table=((100.0, 0.0), (0.0, 
	0.0004375)))

#-----------------------------------------------------------------------
#Definition von "Interactions"
#-----------------------------------------------------------------------
Model.SurfaceToSurfaceContactExp(clearanceRegion=None, 
    createStepName='Einspannung', datumAxis=None, initialClearance=OMIT, 
    interactionProperty='Reibung', master=Model.rootAssembly.instances[
	'Matrize-1'].surfaces['Surf-Oberfläche Matrize'], mechanical
	Constraint=PENALTY, name='Int-Matrize-Blech', slave=Model.root
	Assembly.instances['Blech-1'].surfaces['Surf-untere Oberfläche'], 
	sliding=FINITE)
Model.SurfaceToSurfaceContactExp(clearanceRegion=None, 
    createStepName='Einspannung', datumAxis=None, initialClearance=OMIT, 
    interactionProperty='Reibung', master=Model.rootAssembly.instances[
	'Niederhalter-1'].surfaces['Surf-Oberfläche Niederhalter'], 
	mechanicalConstraint=PENALTY, name='Int-Niederhalter-Blech', slave=
    Model.rootAssembly.instances['Blech-1'].surfaces[
	'Surf-obere Oberfläche'], sliding=FINITE)
	
	
	
	
Model.SurfaceToSurfaceContactExp(clearanceRegion=None, createStepName=
	'Schneidvorgang', datumAxis=None, initialClearance=OMIT, interaction
	Property='Reibung', master=Model.rootAssembly.instances['Stempel-1'].
	surfaces['Surf-Oberfläche Stempel'], mechanicalConstraint=PENALTY, 
	name='Int-Stempel-Blech', slave=Model.rootAssembly.instances[
	'Blech-1'].surfaces['Surf-obere Oberfläche'], sliding=FINITE)
Model.interactions['Int-Stempel-Blech'].setValues(clearanceRegion=None, 
	datumAxis=None, initialClearance=OMIT, interactionProperty=
	'Reibung', mechanicalConstraint=PENALTY, slave=Model.rootAssembly.
	instances['Blech-1'].sets['Set-Blech'], sliding=FINITE)

#-----------------------------------------------------------------------
#Definition von "ALE" 
#-----------------------------------------------------------------------
Model.DisplacementAdaptiveMeshConstraint(amplitude=UNSET, 
    createStepName='Einspannung', localCsys=None, motionType=FOLLOW, 
	name='Ada-ALE_Constraint_links', region=Region(edges=Model.root
	Assembly.instances['Blech-1'].edges.getSequenceFromMask(mask=
	('[#800 ]', ), )), u1=UNSET, u2=UNSET, ur3=UNSET)
Model.DisplacementAdaptiveMeshConstraint(amplitude=UNSET, 
    createStepName='Einspannung', localCsys=None, motionType=FOLLOW, 
	name='Ada-ALE_Constraint_rechts', region=Region(edges=Model.root
	Assembly.instances['Blech-1'].edges.getSequenceFromMask(mask=
	('[#100 ]', ), )), u1=UNSET, u2=UNSET, ur3=UNSET)
Model.AdaptiveMeshControl(equipotentialSmoothingWeight=1.0, name=
	'Ada-ALE_Controls', smoothingAlgorithm=GEOMETRY_ENHANCED)
Model.steps['Einspannung'].AdaptiveMeshDomain(controls=
    'Ada-ALE_Controls', region=Model.rootAssembly.instances['Blech-1'].
	sets['Set-ALE_Bereich'])
Model.steps['Schneidvorgang'].AdaptiveMeshDomain(controls=
    'Ada-ALE_Controls', frequency=3, meshSweeps=3, region=Model.root
	Assembly.instances['Blech-1'].sets['Set-ALE_Bereich'])

#-----------------------------------------------------------------------
#Definition des Jobs
#-----------------------------------------------------------------------
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=
	OFF, memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=
	OFF, multiprocessingMode=DEFAULT, name='Job-Scherschneiden_S10_G33', 
    nodalOutputPrecision=SINGLE, numCpus=2, numDomains=2, 
    parallelizationMethodExplicit=DOMAIN, queue=None, scratch='', type=
	ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)


