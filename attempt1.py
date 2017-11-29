import sys
import urllib.request

from shared import Grid

with urllib.request.urlopen(sys.argv[1]) as req:
    grid = Grid(req)
    print(grid)

    # still working on the grid code currently
