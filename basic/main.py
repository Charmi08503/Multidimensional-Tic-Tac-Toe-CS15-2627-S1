grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]

def display_grid(grid):
    for row in range(3):
        for column in range(3):
            print(" " + grid[row][column], end="")

            if column < 2:
                print(" |", end="")

        print()

        if row < 2:
            print("---+---+---")


def determine_winner(grid):

    # Check rows
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2]:
            return grid[row][0]

    # Check columns
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column]:
            return grid[0][column]

    # Check diagonal from top-left to bottom-right
    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]

    # Check diagonal from top-right to bottom-left
    if grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

    # Check for a tie
    for row in range(3):
        for column in range(3):
            if grid[row][column] == " ":
                return "No winner yet"

    return "Tie"


# Test all four grids

grids = [grid_1, grid_2, grid_3, grid_4]

for number in range(4):
    print("Grid", number + 1)
    display_grid(grids[number])

    winner = determine_winner(grids[number])

    if winner == "Tie":
        print("Winner: Tie")
    elif winner == "No winner yet":
        print("Game is not finished")
    else:
        print("Winner:", winner)

    print()