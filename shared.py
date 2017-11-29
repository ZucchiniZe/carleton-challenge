"""Shared code for all attempts"""

class Grid:
    """Parse and find all quad sequences in a grid of numbers given"""

    def __init__(self, grid):
        self._parse_grid(grid)  # parse the raw text and mutate into grid

        self.height = len(self.grid)  # height is the number of rows (y)
        self.width = len(self.grid[1])  # width is the number of columns (x)

    def __str__(self):
        """a nice pretty print of the grid"""
        return_val = f"height: {self.height}\n"
        return_val += f"width: {self.width}\n\n"
        for row in self.grid:
            for value in row:
                return_val += f"{value}\t"
                # print with tab separator to easily print a nice grid in the
                # terminal
            return_val += '\n'

        return return_val

    def _parse_grid(self, string):
        """
        parse the text grid into a 2d array if integers

        :param string: a string of the grid body
        """
        self.grid = []
        for line in string:
            self.grid.append(self._parse_line(line))

    @staticmethod
    def _parse_line(line):
        """split on white space and then convert to integer"""
        items = line.split()

        return [int(i) for i in items]

    def horiz(self, x, y):
        """
        Get the horizontal quad sequence going right from the point given (with overflow)

        :param x: the x value of where to start
        :param y: the y value of where to start
        :returns: array of 4 values that consist a quad sequence
        """
        # since we are looking at the horizontal axis (x axis) we need to check
        # which way we want to search for a quad sequence to make sure we don't
        # get an out of bounds error

        if x + 3 >= self.width:
            # if we are 3 or closer to the end then just return the entire last
            # quad sequence
            offset = x - (self.width - 4)

            # get how far it is away from the end and then subtract the 4
            # (length of a quad sequence) and then re-query
            return self.horiz(x - offset, y)
        elif x <= self.width:
            # make sure we are not accessing anything smaller
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
        """
        Gets the vertical quad sequence going down from the point given (with overflow)

        :param x: the x value of where to start
        :param y: the y value of where to start
        :returns: array of 4 values that consist a quad sequence
        """
        # pretty much the same logic as the horiz function but with height

        if y + 3 >= self.height:
            offset = y - (self.height - 4)

            return self.vert(x, y - offset)
        elif y <= self.height:
            return [
                self.grid[y][x],
                self.grid[y + 1][x],
                self.grid[y + 2][x],
                self.grid[y + 3][x],
            ]
        else:
            print('the kittens strike back! they killed their killer')
            # again, should never reach here

    def down_diag(self, x, y):
        pass

    def up_diag(self, x, y):
        pass

    def genarate_sequences(self):
        """generator that returns all the quad sequences"""
        pass
