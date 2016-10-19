'''
Find the length of the longest of a special sub-sequence
as defined below through adjacent, non-repeating
cells (including diagonals) in a rectangular grid
of numbers. The special sub-sequence is defined such
that the difference between the current and next
value in the sub-sequence is greater than 3.

For example,
8 2 4
0 6 1
3 7 9

The path can only connect adjacent locations (including diagonals)
and cells may not be repeated. The longest possible
sub-sequence for this example would be of length 8 by
tracing the path 9->1->6->2->8->0->7->3
'''


import sys
import re


# Returns length of the longest path beginning with grid[i][j].
def findLongestFromACell(i, j, grid, visited):
    n = len(grid)
    
    # Base case
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0

    visited.append((i,j))
    curr = 1
    
    # Move to right cell
    if j<n-1 and (abs(grid[i][j] - grid[i][j+1]) > 3) \
        and (i,j+1) not in visited:
        curr = max(1 + findLongestFromACell(i, j+1, grid, visited), curr)

    # Move to left cell
    if j>0 and (abs(grid[i][j] - grid[i][j-1]) > 3) \
        and (i,j-1) not in visited:
        curr = max(1 + findLongestFromACell(i, j-1, grid, visited), curr)
 
    # Move to upper cell
    if i>0 and (abs(grid[i][j] - grid[i-1][j]) > 3) \
        and (i-1,j) not in visited:
        curr = max(1 + findLongestFromACell(i-1, j, grid, visited), curr)
 
    # Move to lower cell
    if i<n-1 and (abs(grid[i][j] - grid[i+1][j]) > 3) \
        and (i+1,j) not in visited:
        curr = max(1 + findLongestFromACell(i+1, j, grid, visited), curr)
       
    # Move to upper-right cell 
    if j<n-1 and i>0 and (abs(grid[i][j] - grid[i-1][j+1]) > 3) \
        and (i-1,j+1) not in visited:
        curr = max(1 + findLongestFromACell(i-1, j+1, grid, visited), curr)
 
    # Move to upper-left cell
    if j>0 and i>0 and (abs(grid[i][j] - grid[i-1][j-1]) > 3) \
        and (i-1,j-1) not in visited:
        curr = max(1 + findLongestFromACell(i-1, j-1, grid, visited), curr)
 
    # Move to lower-right cell
    if i<n-1 and j<n-1 and (abs(grid[i][j] - grid[i+1][j+1]) > 3) \
        and (i+1,j+1) not in visited:
        curr = max(1 + findLongestFromACell(i+1, j+1, grid, visited), curr)
 
    # Move to lower-left cell
    if i<n-1 and j>0 and (abs(grid[i][j] - grid[i+1][j-1]) > 3) \
        and (i+1,j-1) not in visited:
        curr = max(1 + findLongestFromACell(i+1, j-1, grid, visited), curr)
 
    visited.pop()
    return curr


# Returns length of the longest path beginning with any cell
def longest_subsequence(grid):
    """
    Take a rectangular grid of numbers and find the length
    of the longest sequence of numbers.
    Return the length as an integer.
    """
    # Initialize result
    result = 1
    n = len(grid)

    # Compute longest path beginning from all cells
    for i in range(n):
        for j in range(n):
            visited = []
            curr = findLongestFromACell(i, j, grid, visited)
            if curr > result:
                result = curr

    return result


def main():
    grid = [[8, 2, 4], 
            [0, 6, 1],
            [3, 7, 9]]

    res = longest_subsequence(grid)
    print(str(res) + "\n")

if __name__ == "__main__":
    main()
