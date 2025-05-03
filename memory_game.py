import random

# Welcome message
print("Welcome to memory game!")

# Create a list of fruits, cars, and colors
fruits = ["Apple", "Banana", "Kiwi", "Mango"]
cars = ["Ford", "Toyota", "Nissan", "Mazda"]
colors = ["Red", "Green", "Blue", "Yellow"]

# Combine and duplicate the list to have pairs
cell_values = (fruits + cars + colors) * 2
random.shuffle(cell_values)

# Define board dimensions
N = 4
M = 4

# Create the game board by slicing the shuffled list
board = []
for i in range(N):
    row = cell_values[i * M:(i + 1) * M]
    board.append(row)

# Initialize the display board with "?" for hidden cells
display_board = [["?" for _ in range(M)] for _ in range(N)]

# Function to check if the game is over (no more "?" left)
def is_game_over(display):
    for row in display:
        if "?" in row:
            return False
    return True

# Main game loop
while not is_game_over(display_board):
    # Print the current display board
    for row in display_board:
        print(" ".join(row))

    # Input for the first cell
    cell1_line = int(input(f"Choose line for cell 1 (0-{N - 1}): "))
    cell1_row = int(input(f"Choose row for cell 1 (0-{M - 1}): "))
    # Ensure the first cell is not already revealed
    while display_board[cell1_line][cell1_row] != "?":
        print("Cell already revealed. Choose another.")
        cell1_line = int(input(f"Choose line for cell 1 (0-{N - 1}): "))
        cell1_row = int(input(f"Choose row for cell 1 (0-{M - 1}): "))

    # Input for the second cell
    cell2_line = int(input(f"Choose line for cell 2 (0-{N - 1}): "))
    cell2_row = int(input(f"Choose row for cell 2 (0-{M - 1}): "))
    # Ensure the second cell is not the same as the first and not revealed
    while (cell2_line, cell2_row) == (cell1_line, cell1_row) or display_board[cell2_line][cell2_row] != "?":
        print("Invalid choice. Choose another cell.")
        cell2_line = int(input(f"Choose line for cell 2 (0-{N - 1}): "))
        cell2_row = int(input(f"Choose row for cell 2 (0-{M - 1}): "))

    # Reveal chosen cells
    cell1 = board[cell1_line][cell1_row]
    cell2 = board[cell2_line][cell2_row]
    print(f"Cell 1: {cell1}\nCell 2: {cell2}")

    # If a match, update display board
    if cell1 == cell2:
        print("Match!")
        display_board[cell1_line][cell1_row] = cell1
        display_board[cell2_line][cell2_row] = cell2
    else:
        print("No match.")

# Game complete
print("Congratulations! You finished the game!")

# ---------------------------------------------------
# Software Considerations:

# Reliability:
# - The game checks if cells are already revealed or if the same cell is picked twice.
# - It only updates the display board when valid selections are made.
# - The loop only ends when all cells are correctly matched.

# Maintainability:
# - Code is structured into clear sections: setup, input validation, game logic.
# - Good naming conventions (e.g., cell1_line, cell2_row) help in understanding the purpose of variables.
# - Functions are used (e.g., is_game_over) to separate logic and make code easier to manage and extend.

# Scalability:
# - Changing the board size (N, M) or the list of items requires minimal changes.
# - The program adapts to different numbers of items automatically (due to slicing and dynamic board creation).
