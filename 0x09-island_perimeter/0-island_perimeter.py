#!/usr/bin/python3

"""
Island perimeter
"""


def island_perimeter(grid):
    """Determine the island's perimeter using the grid.

    Args:
        grid (list[list[int]]): A 2D grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    perimeter = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Checks left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
    return perimeter
