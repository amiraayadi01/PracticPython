# Check Tic Tac Toe
# Topics: Lists of Lists
winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

def grid(grid):

    for i in range(0, 3):
        row = {grid[i][0], grid[i][1], grid[i][2]}
        if len(row) == 1 and grid[i][0] != 0:
            return grid[i][0]

    for i in range(0, 3):
        column = {grid[0][i], grid[1][i], grid[2][i]}
        if len(column) == 1 and grid[0][i] != 0:
            return grid[0][i]

    diag1 = {grid[0][0], grid[1][1], grid[2][2]}
    diag2 = {grid[0][2], grid[1][1], grid[2][0]}
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]

print(grid(winner_is_1))