__title__ = "Lock Grids"
__authors__ = ["Junaid"]

from Autodesk.Revit.DB import FilteredElementCollector, Grid, Transaction

# Get the current document
doc = __revit__.ActiveUIDocument.Document

# Get all grids
grids = FilteredElementCollector(doc).OfClass(Grid).ToElements()

# Start transaction
t = Transaction(doc, "Pin All Grids")
t.Start()

for grid in grids:
    if not grid.Pinned:
        grid.Pinned = True
        print("Pinned Grid: }".format(grid.Name))

t.Commit()

print("Pinned {} Grid(s).".format(len(grids)))
