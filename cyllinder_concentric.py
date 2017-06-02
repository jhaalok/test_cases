#!/usr/bin/env python
#!/usr/local/lib/python3.4 


import sys
salome.salome_init()
import GEOM
import salome
import math

from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)
theStudy = salome.myStudy
import salome_notebook
notebook = salome_notebook.notebook

gg = salome.ImportComponentGUI("GEOM")

# BHA components parameters
Wellbore = 10  # m
OD_Component = 6.5  # m
#ID_Component = 10 # m
Length_Component = 20 # m

# Converting imperial units to SI
# Wellbore = Wellbore*0.0254
# OD_Component = OD_Component*0.0254
# ID_Component = ID_Component*0.0254


# Base vector for rotation and extrusion

Origin = geompy.MakeVertex (0,0,0)
EndVector = geompy.MakeVertex (0,0,1)
Vector = geompy.MakeVector(Origin ,EndVector)

# Base line for wellbore annular
pOD = geompy.MakeVertex(OD_Component,0,0)
pWell = geompy.MakeVertex(Wellbore,0,0)
vAnnular = geompy.MakeVector(pOD,pWell)

# Base annular disc
wAnnular = geompy.MakeWire([vAnnular])
revolution = geompy.MakeRevolution(wAnnular, Vector, 2*math.pi)
Annular = geompy.MakePrismVecH(revolution, Vector, Length_Component)
id_Annular = geompy.addToStudy(Annular , "Annular")


# BHA component parameters for inner cyllinder
Wellbore1 = 2  # m
OD_Component1 = 2.5  # m
ID_Component = 10 # m
Length_Component1 = 20 # m


# Base vector for rotation and extrusion of inner cyllinder
Origin1 = geompy.MakeVertex (3,0,0)
EndVector1 = geompy.MakeVertex (3,0,1)
Vector1 = geompy.MakeVector(Origin1 ,EndVector1)

# Base line for wellbore annular_inner cyllinder
pOD1 = geompy.MakeVertex(OD_Component1,0,0)
pWell1 = geompy.MakeVertex(Wellbore1,0,0)
vAnnular1 = geompy.MakeVector(pOD1,pWell1)

# Base annular disc_inner cyllinder
wAnnular1 = geompy.MakeWire([vAnnular1])
revolution1 = geompy.MakeRevolution(wAnnular1, Vector1, 2*math.pi)
Annular1 = geompy.MakePrismVecH(revolution1, Vector1, Length_Component1)
id_Annular = geompy.addToStudy(Annular1 , "Annular1")

[Inlet,Inner_Wall,Outer_Wall,Outlet] = geompy.ExtractShapes(Annular, geompy.ShapeType["FACE"], True)
#[Inlet1,Inner_Wall1,Outer_Wall1,Outlet1] = geompy.ExtractShapes(Annular1, geompy.ShapeType["FACE"], True)

#geompy.addToStudyInFather( Annular, Inlet, 'Inlet', Annular1, Inlet1, 'Inlet1')
geompy.addToStudyInFather( Annular, Inlet, 'Inlet')
geompy.addToStudyInFather( Annular1, Inlet1, 'Inlet1')

#geompy.addToStudyInFather( Annular, Inner_Wall, 'Inner_Wall', Annular1, Inner_Wall1, 'Inner_Wall1')
geompy.addToStudyInFather( Annular, Inner_Wall, 'Inner_Wall')
geompy.addToStudyInFather( Annular1, Inner_Wall1, 'Inner_Wall1')

#geompy.addToStudyInFather( Annular, Outer_Wall, 'Outer_Wall', Annular1, Outer_Wall1, 'Outer_Wall1')
geompy.addToStudyInFather( Annular, Outer_Wall, 'Outer_Wall')
geompy.addToStudyInFather( Annular1, Outer_Wall1, 'Outer_Wall1')

#geompy.addToStudyInFather( Annular, Outlet, 'Outlet', Annular1, Outlet1, 'Outlet1')
geompy.addToStudyInFather( Annular, Outlet, 'Outlet')
geompy.addToStudyInFather( Annular1, Outlet1, 'Outlet1')

#[Inlet1,Inner_Wall1,Outer_Wall1,Outlet1] = geompy.ExtractShapes(Annular, geompy.ShapeType["FACE"], True)
geompy.addToStudyInFather( Annular1, Inlet1, 'Inlet1' )
geompy.addToStudyInFather( Annular1, Inner_Wall1, 'Inner_Wall1' )
geompy.addToStudyInFather( Annular1, Outer_Wall1, 'Outer_Wall1' )
geompy.addToStudyInFather( Annular1, Outlet1, 'Outlet1' )

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)

###################

