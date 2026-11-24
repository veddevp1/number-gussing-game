"""
CodeOrbit Tech - Task 3: Number Guessing Game
Guess a random number, receive hints, and track attempts.
"""

import random


def play_round():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if not 1 <= guess <= 100:
                print("Please enter a number from 1 to 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Correct! You guessed it in {attempts} attempt(s).")
                return

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=== NUMBER GUESSING GAME ===")

    while True:
        play_round()
        again = input("\nWould you like to play another round? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
