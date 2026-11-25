
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
        if grid[row][0] != " " and grid[row][0] == grid[row][1] == grid[row][2]:
            return grid[row][0]

    # Check columns
    for column in range(3):
        if grid[0][column] != " " and grid[0][column] == grid[1][column] == grid[2][column]:
            return grid[0][column]

    # Check diagonal from top-left to bottom-right
    if grid[0][0] != " " and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]

    # Check diagonal from top-right to bottom-left
    if grid[0][2] != " " and grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

    # Check for empty spaces
    for row in range(3):
        for column in range(3):
            if grid[row][column] == " ":
                return "No winner yet"

    return "Tie"


# Create an empty 3x3 board
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Set the first player
current_player = "X"

# Display the starting board
print("Welcome to Tic-Tac-Toe!")
display_grid(grid)

winner = "No winner yet"

# Continue until there is a winner or tie
while winner == "No winner yet":

    print()
    print("Player", current_player + "'s turn")

    # Get valid row and column input
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            column = int(input("Enter column (0-2): "))

            # Check if coordinates are valid
            if row < 0 or row > 2 or column < 0 or column > 2:
                print("Invalid coordinates. Try again.")

            # Check if the space is occupied
            elif grid[row][column] != " ":
                print("That space is already occupied. Try again.")

            else:
                break

        except ValueError:
            print("Please enter numbers only. Try again.")

    # Place the player's mark
    grid[row][column] = current_player

    # Display the updated board
    print()
    display_grid(grid)

    # Check for a winner or tie
    winner = determine_winner(grid)

    # Switch players if the game is not over
    if winner == "No winner yet":
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Display the final result
print()

if winner == "Tie":
    print("The game ended in a tie!")
else:
    print("Player", winner, "wins!")
