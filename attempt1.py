import sys
import urllib.request

import shared

with urllib.request.urlopen(sys.argv[1]) as req:
    grid = shared.Grid(req)
    print(grid)

    # still working on the grid code currently
