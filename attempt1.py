import sys
import urllib.request

import grid

def run(url):
    return urllib.request.urlopen(url)

# with auto closes the resource
with run(sys.argv[1]) as req:
    current = grid.Grid(req)

    print(current)


    ### actual code for solving begins here
