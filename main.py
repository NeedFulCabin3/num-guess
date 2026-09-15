import random

def get_valid_integer(prompt: str) -> int:
    """Prompt the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print("=== Welcome to the Number Guessing Game! ===")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print("Can you guess what it is?\n")

    while True:
        guess = get_valid_integer("Enter your guess: ")
        attempts += 1

        if guess < lower_bound or guess > upper_bound:
            print(f"Out of range! Please guess between {lower_bound} and {upper_bound}.")
            continue

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"\nCongratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempt(s).")
            break


if __name__ == "__main__":
    main()