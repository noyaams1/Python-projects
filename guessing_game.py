import random

print("Welcome to the guessing game!")

while True:
    random_number = random.randint(1, 20)
    max_tries = 5
    user_tries = 0

    while user_tries < max_tries:
        try:
            user_guess = int(input("Guess the number (between 1 and 20): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess > random_number:
            print("Too high!")
        elif user_guess < random_number:
            print("Too low!")
        else:
            print("Correct! You guessed it!")
            break

        user_tries += 1
    else:
        print(f"Game over. The correct number was: {random_number}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
