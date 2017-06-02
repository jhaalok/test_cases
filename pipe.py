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
Wellbore = 5  # m
OD_Component = 6.5  # m
ID_Component = 1 # m
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

[Inlet,Inner_Wall,Outer_Wall,Outlet] = geompy.ExtractShapes(Annular, geompy.ShapeType["FACE"], True)
geompy.addToStudyInFather( Annular, Inlet, 'Inlet' )
geompy.addToStudyInFather( Annular, Inner_Wall, 'Inner_Wall' )
geompy.addToStudyInFather( Annular, Outer_Wall, 'Outer_Wall' )
geompy.addToStudyInFather( Annular, Outlet, 'Outlet' )

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)

###################

