import random

def controls():
    direction = input("Enter move (w/a/s/d): ")
    if direction in ['w', 'a', 's', 'd']:
        return direction
    else:
        print("Invalid move. Please enter w, a, s, or d.")
        return controls()

def moves(direction):
    if direction == 'a':  # left
        for i in range(size):
            new_row = [num for num in grid[i] if num != 0]
            new_row += [0] * (size - len(new_row))
            grid[i] = new_row
    elif direction == 'd':  # right
        for i in range(size):
            new_row = [num for num in grid[i] if num != 0]
            new_row = [0] * (size - len(new_row)) + new_row
            grid[i] = new_row
    elif direction == 'w':  # up
        for j in range(size):
            new_col = [grid[i][j] for i in range(size) if grid[i][j] != 0]
            new_col += [0] * (size - len(new_col))
            for i in range(size):
                grid[i][j] = new_col[i]
    elif direction == 's':  # down
        for j in range(size):
            new_col = [grid[i][j] for i in range(size) if grid[i][j] != 0]
            new_col = [0] * (size - len(new_col)) + new_col
            for i in range(size):
                grid[i][j] = new_col[i]

def merging():


size = 4
grid = [[0 for i in range(size)] for j in range(size)]
grid [random.randint(0, 3)][random.randint(0, 3)] = 2
for row in grid:
    print(row)
while True:
    direction = controls()
    moves(direction)
    merging()
    moves(direction)
    empty_cells = [(i, j) for i in range(size) for j in range(size) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2
    for row in grid:
        print(row)