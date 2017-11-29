class Grid:
    def __init__(self, grid):
        self._parse_grid(grid)  # parse the resp and mutate into grid

        self.height = len(self.grid)  # height is the number of rows (y)
        self.width = len(self.grid[1])  # width is the number of columns (x)

    def _parse_grid(self, string):
        """parse the text grid into a 2d array if integers"""
        self.grid = []
        for line in string:
            self.grid.append(self._parse_line(line))

    def _parse_line(self, line):
        """split on white space and then convert to integer"""
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

    def horiz(self, x, y):
        # since we are looking at the horizontal axis (x axis) we need to check
        # which way we want to search for a quad sequence to make sure we don't
        # get an out of bounds error

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
            print('you murdered a bunch of kittens you monster')
            # should never get here (save the kitties)

    def vert(self, x, y):
        # pretty much the same logic as the horiz function but with height

        if y + 3 >= self.height:
            offset = y - (self.height - 4)

            return self.vert(x, y - offset)
        elif y + 3 <= self.height:
            return [
                self.grid[y][x],
                self.grid[y + 1][x],
                self.grid[y + 2][x],
                self.grid[y + 3][x],
            ]
        else:
            print('the kittens strike back! they killed their killer')
            # again, should never reach here
