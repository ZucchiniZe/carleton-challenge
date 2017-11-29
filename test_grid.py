import pytest

import urllib.request
import grid as parser


@pytest.fixture
def grid():
    """returns a the text contents of the sample grid"""
    url = 'http://cs.carleton.edu/faculty/dln/placement/grid.txt'

    # have the fixture function close the resource for us for cleaner code
    with urllib.request.urlopen(url) as req:
        yield parser.Grid(req)


def test_first_horizontal(grid):
    """get the first quad sequence horizontally"""
    assert grid.horiz(0, 0) == [674, 20, 305, -921]


def test_11th_horizontal(grid):
    """should get the last 4 numbers of the first row in the grid"""
    assert grid.horiz(11, 0) == [-123, -620, -88, 269]


def test_14th_horizontal(grid):
    """since 14th number is 3 away from the end we need to return all 4 numbers at the end"""
    # should be  the same as the 11th x
    assert grid.horiz(14, 0) == [-123, -620, -88, 269]
