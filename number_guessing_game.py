import random


def main():
    input("Welcome to number guessing game 🔢 press enter to start ✅")

    min_number = int(input("Enter the min number: "))
    max_number = int(input("Enter the max number: "))
    attempts = 0
    hint = ""

    random_number = random.randint(min_number, max_number)
    print(f"The computer chose random number between {min_number} and {max_number}.")

    while True:
        user_guess = int(input("Your Guess: "))
        attempts += 1
        if user_guess == random_number:
            print(f"You guessed it right with {attempts} attempts")
            break

        if user_guess > random_number:
            hint = "the number is lower."
        elif user_guess < random_number:
            hint = "the number is higher."
        print(f"Try again, {hint}")


if __name__ == "__main__":
    main()
