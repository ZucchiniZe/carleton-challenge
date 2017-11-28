import sys
import urllib.request


class Grid:
    def __init__(self, grid):
        self._parse_grid(grid)  # parse the resp and mutate into grid
        self.height = len(self.grid)  # height is the number of rows (y)
        self.width = len(self.grid[1])  # width is the number of columns (x)

    def _parse_grid(self, string):
        self.grid = []
        for line in string:
            self.grid.append(self._parse_line(line))

    def _parse_line(self, line):
        items = line.split()

        return [int(i) for i in items]

    def __str__(self):
        """a nice pretty print of the grid"""
        return_val = f"height: {self.height}\nwidth: {self.width}\n\n"
        for row in self.grid:
            for value in row:
                return_val += f"{value}\t"  # print with tab separator to easily print a nice grid in the terminal
            return_val += '\n'

        return return_val

    def horiz(self, x, y, rec=False):
        # since we are looking at the horizontal axis (x axis) we need to check
        # which way we want to search for a quad sequence to make sure we don't
        # get an out of bounds error
        if rec:
            return None

        if x + 3 >= self.width:  # first branch: if we are 3 or closer to the end then just return the last 4
            offset = x - (self.width - 4)
            # get how far it is away from the end and then subtract the quad and then re-query

            return self.horiz(x - offset, y)
        elif x + 3 <= self.width:  # second branch: if we are 3 or closer to the beginning
            return [
                self.grid[y][x],
                self.grid[y][x + 1],
                self.grid[y][x + 2],
                self.grid[y][x + 3],
            ]
        else:
            print('you murdered a bunch of kittens you monster'
                  )  # should never get here (save them kitties)

    def gen_sequences(self):
        """Should generate a list of possible sequences"""
        pass


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.urlopen(url)

    # with auto closes the resource
    with urllib.request.urlopen(url) as req:
        grid = Grid(req)
        print(grid)
        print(grid.horiz(2, 0))
