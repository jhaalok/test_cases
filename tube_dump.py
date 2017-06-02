# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.8.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/user01/SALOME-7.8.0-OPENSOURCE-DB08/test_cases')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Vector_1 = geompy.MakeVectorDXDYDZ(0, 0, 500)
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
geomObj_2 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
geomObj_3 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
#outer = geompy.MakeDividedCylinder(100, 300, GEOM.HEXAGON)
inner = geompy.MakeDividedCylinder(95, 300, GEOM.HEXAGON)
#inner = geompy.MakeDividedCylinder(95, 300, GEOM.OCTAGON)
[Solid_1, Solid_2, Solid_3, Solid_4, Solid_5, Solid_6, Solid_7, Solid_8, Solid_9, Solid_10, Solid_11, Solid_12, Solid_13, Solid_14, Solid_15, Solid_16, Solid_17, Solid_18] = geompy.MakeBlockExplode(inner, 6, 6)
[Solid_19, Solid_20, Solid_21, Solid_22, Solid_23, Solid_24, Solid_25, Solid_26, Solid_27, Solid_28, Solid_29, Solid_30, Solid_31, Solid_32, Solid_33, Solid_34, Solid_35, Solid_36] = geompy.MakeBlockExplode(inner, 6, 6)
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
listSubShapeIDs = geompy.SubShapeAllIDs(inner, geompy.ShapeType["SOLID"])
tube = geompy.CreateGroup(inner, geompy.ShapeType["SOLID"])
geompy.UnionIDs(tube, [2, 36, 77, 101, 135, 159, 193, 217, 251, 275, 309, 333])
[Face_1,Face_2,Face_3,Face_4,Face_5,Face_6,Face_7,Face_8,Face_9,Face_10,Face_11,Face_12] = geompy.SubShapes(tube, [128, 80, 32, 248, 104, 56, 200, 286, 272, 224, 176, 152])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
[Face_13,Face_14,Face_15,Face_16,Face_17,Face_18,Face_19,Face_20,Face_21,Face_22,Face_23,Face_24] = geompy.SubShapes(tube, [288, 82, 58, 106, 202, 226, 154, 178, 34, 250, 274, 130])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(tube, geompy.ShapeType["FACE"])
[geomObj_4,geomObj_5,geomObj_6,geomObj_7,geomObj_8,geomObj_9,geomObj_10,geomObj_11,geomObj_12,geomObj_13,geomObj_14,geomObj_15] = geompy.SubShapes(tube, [104, 128, 152, 176, 200, 224, 248, 272, 286, 32, 56, 80])
outlet = geompy.CreateGroup(tube, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [128, 80, 32, 248, 104, 56, 200, 286, 272, 224, 176, 152])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_24, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_24, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_24, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_24, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_24, geompy.ShapeType["FACE"])
inlet = geompy.CreateGroup(tube, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, [288, 82, 58, 106, 202, 226, 154, 178, 34, 250, 274, 130])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vector_1, 'Vector_1' )
geompy.addToStudyInFather( inner, Solid_5, 'Solid_5' )
#geompy.addToStudy( outer, 'outer' )
geompy.addToStudy( inner, 'inner' )
geompy.addToStudyInFather( inner, Solid_3, 'Solid_3' )
geompy.addToStudyInFather( inner, Solid_4, 'Solid_4' )
geompy.addToStudyInFather( inner, Solid_2, 'Solid_2' )
geompy.addToStudyInFather( inner, Solid_1, 'Solid_1' )
geompy.addToStudyInFather( inner, Solid_6, 'Solid_6' )
geompy.addToStudyInFather( inner, Solid_7, 'Solid_7' )
geompy.addToStudyInFather( inner, Solid_8, 'Solid_8' )
geompy.addToStudyInFather( inner, Solid_9, 'Solid_9' )
geompy.addToStudyInFather( inner, Solid_10, 'Solid_10' )
geompy.addToStudyInFather( inner, Solid_11, 'Solid_11' )
geompy.addToStudyInFather( inner, Solid_12, 'Solid_12' )
geompy.addToStudyInFather( inner, Solid_13, 'Solid_13' )
geompy.addToStudyInFather( inner, Solid_14, 'Solid_14' )
geompy.addToStudyInFather( inner, Solid_15, 'Solid_15' )
geompy.addToStudyInFather( inner, Solid_16, 'Solid_16' )
geompy.addToStudyInFather( inner, Solid_17, 'Solid_17' )
geompy.addToStudyInFather( inner, Solid_18, 'Solid_18' )
geompy.addToStudyInFather( inner, Solid_19, 'Solid_19' )
geompy.addToStudyInFather( inner, Solid_20, 'Solid_20' )
geompy.addToStudyInFather( inner, Solid_21, 'Solid_21' )
geompy.addToStudyInFather( inner, Solid_22, 'Solid_22' )
geompy.addToStudyInFather( inner, Solid_23, 'Solid_23' )
geompy.addToStudyInFather( inner, Solid_24, 'Solid_24' )
geompy.addToStudyInFather( inner, Solid_25, 'Solid_25' )
geompy.addToStudyInFather( inner, Solid_26, 'Solid_26' )
geompy.addToStudyInFather( inner, Solid_27, 'Solid_27' )
geompy.addToStudyInFather( inner, Solid_28, 'Solid_28' )
geompy.addToStudyInFather( inner, Solid_29, 'Solid_29' )
geompy.addToStudyInFather( inner, Solid_30, 'Solid_30' )
geompy.addToStudyInFather( inner, Solid_31, 'Solid_31' )
geompy.addToStudyInFather( inner, Solid_32, 'Solid_32' )
geompy.addToStudyInFather( inner, Solid_33, 'Solid_33' )
geompy.addToStudyInFather( inner, Solid_34, 'Solid_34' )
geompy.addToStudyInFather( inner, Solid_35, 'Solid_35' )
geompy.addToStudyInFather( inner, Solid_36, 'Solid_36' )
geompy.addToStudyInFather( inner, tube, 'tube' )
geompy.addToStudyInFather( tube, Face_1, 'Face_1' )
geompy.addToStudyInFather( tube, Face_2, 'Face_2' )
geompy.addToStudyInFather( tube, Face_3, 'Face_3' )
geompy.addToStudyInFather( tube, Face_4, 'Face_4' )
geompy.addToStudyInFather( tube, Face_5, 'Face_5' )
geompy.addToStudyInFather( tube, Face_6, 'Face_6' )
geompy.addToStudyInFather( tube, Face_7, 'Face_7' )
geompy.addToStudyInFather( tube, Face_8, 'Face_8' )
geompy.addToStudyInFather( tube, Face_9, 'Face_9' )
geompy.addToStudyInFather( tube, Face_10, 'Face_10' )
geompy.addToStudyInFather( tube, Face_11, 'Face_11' )
geompy.addToStudyInFather( tube, Face_12, 'Face_12' )
geompy.addToStudyInFather( tube, outlet, 'outlet' )
geompy.addToStudyInFather( tube, Face_13, 'Face_13' )
geompy.addToStudyInFather( tube, Face_14, 'Face_14' )
geompy.addToStudyInFather( tube, Face_15, 'Face_15' )
geompy.addToStudyInFather( tube, Face_16, 'Face_16' )
geompy.addToStudyInFather( tube, Face_17, 'Face_17' )
geompy.addToStudyInFather( tube, Face_18, 'Face_18' )
geompy.addToStudyInFather( tube, Face_19, 'Face_19' )
geompy.addToStudyInFather( tube, Face_20, 'Face_20' )
geompy.addToStudyInFather( tube, Face_21, 'Face_21' )
geompy.addToStudyInFather( tube, Face_22, 'Face_22' )
geompy.addToStudyInFather( tube, Face_23, 'Face_23' )
geompy.addToStudyInFather( tube, Face_24, 'Face_24' )
geompy.addToStudyInFather( tube, inlet, 'inlet' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(tube)
Regular_1D = Mesh_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(15)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
isDone = Mesh_1.Compute()
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_FreeFaces,SMESH.FT_Undefined,0)
aCriteria.append(aCriterion)
inlet_1 = Mesh_1.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outlet_1 = Mesh_1.GroupOnGeom(outlet,'outlet',SMESH.FACE)
#walls = Mesh_1.GetMesh().CutListOfGroups( [ smeshObj_1 ], [ inlet_1, outlet_1 ], 'walls' ) ### smeshObj_1 has not been yet created
try:
  Mesh_1.ExportUNV( r'/home/user01/tube.unv' )
except:
  print 'ExportUNV() failed. Invalid file name?'
try:
  Mesh_1.ExportUNV( r'/home/user01/SALOME-7.8.0-OPENSOURCE-DB08/test_cases/tube.unv' )
except:
  print 'ExportUNV() failed. Invalid file name?'


## Set names of Mesh objects
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
