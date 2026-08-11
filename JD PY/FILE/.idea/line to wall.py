import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

doc = __revit__.ActiveUIDocument.Document

# --- Get a 300 mm wall type ---
wall_types = FilteredElementCollector(doc).OfClass(WallType).ToElements()
wall_type_300 = None
for wt in wall_types:
    if abs(wt.Width - 0.3) < 0.001:  # 0.3 m = 300 mm
        wall_type_300 = wt
        break

if not wall_type_300:
    raise Exception("No 300 mm wall type found. Please create one in Revit first.")

# --- Get a level ---
level = FilteredElementCollector(doc).OfClass(Level).FirstElement()

# --- Collect model lines ---
model_lines = FilteredElementCollector(doc).OfClass(CurveElement).ToElements()

# --- Collect door and window family symbols ---
door_symbols = FilteredElementCollector(doc).OfClass(FamilySymbol).OfCategory(BuiltInCategory.OST_Doors).ToElements()
window_symbols = FilteredElementCollector(doc).OfClass(FamilySymbol).OfCategory(BuiltInCategory.OST_Windows).ToElements()

door_symbol = door_symbols[0] if door_symbols else None
window_symbol = window_symbols[0] if window_symbols else None

# Activate symbols if needed
if door_symbol and not door_symbol.IsActive:
    door_symbol.Activate()
if window_symbol and not window_symbol.IsActive:
    window_symbol.Activate()

walls_created = []
doors_created = []
windows_created = []

with Transaction(doc, "Convert Lines to 300mm Walls + Doors/Windows") as t:
    t.Start()
    for line in model_lines:
        curve = line.GeometryCurve
        try:
            # Create wall
            wall = Wall.Create(doc, curve, wall_type_300.Id, level.Id, 3.0, 0.0, False, False)  # 3m height
            walls_created.append(wall)

            # Midpoint of wall curve
            midpoint = curve.Evaluate(0.5, True)

            # Place door at midpoint (if available)
            if door_symbol:
                door_instance = doc.Create.NewFamilyInstance(midpoint, door_symbol, wall, level, StructuralType.NonStructural)
                doors_created.append(door_instance)

            # Place window slightly offset (if available)
            if window_symbol:
                offset_point = curve.Evaluate(0.25, True)  # quarter point
                window_instance = doc.Create.NewFamilyInstance(offset_point, window_symbol, wall, level, StructuralType.NonStructural)
                windows_created.append(window_instance)

        except Exception as e:
            print("Could not create wall/door/window from line {}: {}".format(line.Id, str(e)))
    t.Commit()

print("Created {} wall(s), {} door(s), and {} window(s).".format(len(walls_created), len(doors_created), len(windows_created)))
