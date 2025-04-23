import random

# Print welcome message
print("Welcome to Boxing Simulator!")

# Explain the moves
print("Choose your boxing move:")
print("1: Jab")
print("2: Cross")
print("3: Hook")
print("4: Uppercut")

# Ask for number of rounds
rounds = int(input("How many rounds do you want to fight? (3, 6, or 12): "))

# Initialize scores
player_score = 0
opponent_score = 0

# Fight loop
for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}!")

    # Player chooses move
    player_move = int(input("Choose your move (1-4): "))
    while player_move < 1 or player_move > 4:
        player_move = int(input("Invalid! Choose 1-4: "))

    # Computer chooses random move
    opponent_move = random.randint(1, 4)
    print(f"Opponent chose: {opponent_move}")

    # Determine who wins
    if player_move == opponent_move:
        print("Draw! No points.")
    elif (player_move == 1 and opponent_move == 3) or \
            (player_move == 2 and opponent_move == 1) or \
            (player_move == 3 and opponent_move == 4) or \
            (player_move == 4 and opponent_move == 2):
        print("You win this round!")
        player_score += 1
    else:
        print("Opponent wins this round!")
        opponent_score += 1

# Final results
print("\nFight Over!")
print(f"Your score: {player_score}")
print(f"Opponent score: {opponent_score}")

if player_score > opponent_score:
    print("You are the champion!")
elif opponent_score > player_score:
    print("You lost... better luck next time!")
else:
    print("It's a tie!")

