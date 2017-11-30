import pytest

from shared import Grid


@pytest.fixture
def grid():
    """returns a the text contents of the sample grid"""
    # have the fixture function close the resource for us to result in cleaner
    # code
    with open('test_grid.txt', 'r') as body:
        yield Grid(body)  # just return a parsed grid


def test_grid_props(grid):
    """test the computed properties on the grid"""
    assert grid.height == 10
    assert grid.width == 15


def test_regular_horizontal(grid):
    """test the regular horizontal quad sequence"""
    assert grid.horiz(0, 0) == [674, 20, 305, -921]
    assert grid.horiz(3, 0) == [-921, 912, 779, 25]


def test_overflow_horizontal(grid):
    """test the overflow of the horizontal"""
    last4 = [-123, -620, -88, 269]

    assert grid.horiz(11, 0) == last4
    assert grid.horiz(14, 0) == last4

    assert grid.horiz(11, 0) == grid.horiz(14, 0)


def test_regular_vertical(grid):
    """test the regular vertical quad sequence"""
    assert grid.vert(0, 0) == [674, 650, 30, -140]
    assert grid.vert(0, 3) == [-140, 753, -662, 823]


def test_overflow_vertical(grid):
    """test the overflow of the vertical"""
    last4 = [823, -385, -540, 44]

    assert grid.vert(0, 7) == last4
    assert grid.vert(0, 10) == last4

    assert grid.vert(0, 7) == grid.vert(0, 10)


def test_regular_down_diagonal(grid):
    """test the regular downward diagonal quad sequence"""
    assert grid.down_diag(0, 0) == [674, 640, 649, 230]
    assert grid.down_diag(1, 0) == [20, 613, 959, -638]


def test_overflow_down_diagonal(grid):
    """test the overflow of the downward diagonal quad sequence"""
    last_lower4 = [823, 562, 917, -533]

    assert grid.down_diag(0, 7) == last_lower4
    assert grid.down_diag(0, 8) == last_lower4
    assert grid.down_diag(0, 9) == last_lower4

    assert grid.down_diag(0, 7) == grid.down_diag(0, 9)

    last_upper4 = [-123, -863, 607, 547]

    assert grid.down_diag(11, 0) == last_upper4
    assert grid.down_diag(12, 0) == last_upper4
    assert grid.down_diag(13, 0) == last_upper4

    assert grid.down_diag(11, 0) == grid.down_diag(13, 0)
