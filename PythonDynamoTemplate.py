# Made by Dave Wilson
# Free for use
# Computational Designer | www.davidwilson.xyz

#common language runtime
#.dll = dynamic link library - Tells the program how to do something.

import clr
import sys.path.append("C:\Program Files (x86)\IronPython 2.7\Lib")
import System
from System import Array
from Sytem.Collection.Generic import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

import Autodesk 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager 

# Current doc/app/ui
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument

#element = Unwrapelement(IN[0])

# Do some action in a Transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# your actions
TransactionManager.Instance.TransactionTaskDone()


#element.ToDSType(True) #Not created in script. Revit Owned
#element.ToDSType(False) #Created in script. Dynamo Owned

#OUT = dir(Wall)
#OUT = Wall.__doc__
#OUT = Wall.Id.__doc__
#OUT = Wall.Id.__name__
#OUT = Wall.Geometry.Item
#OUT = dir(Vector)
#OUT = Vector.Add.__doc__
