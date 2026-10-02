"""Task 2: Number Guessing Game (with attempt counter)"""
import random


def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("=== Number Guessing Game ===\nI'm thinking of a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter a whole number.")
            continue
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempt(s).")
            break


if __name__ == "__main__":
    main()
