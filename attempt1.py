import sys
import urllib.request

import grid as gridlib

with urllib.request.urlopen(sys.argv[1]) as req:
    grid = gridlib.Grid(req)
    print(grid)

    # still working on the grid code currently
