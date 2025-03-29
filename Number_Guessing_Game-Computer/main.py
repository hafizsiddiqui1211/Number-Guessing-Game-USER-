import random as rd


def guess_the_number():
    """Guess the number game by Computer"""
    number = rd.randint(0, 100)
    guesses_left = 7
    print(
        "Welcome to the number Guessing Game"
    )
    print(
        "I'm thinking of a number between 0 and 100. You have 7 tries to guess it."
    )
    while guesses_left > 0:
        print(f"You've {guesses_left} guesses left.")
        try:
            guess = int(input("Enter your guess: "))
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(
                    f"🎉Congratulations! You guessed the number {number} correctly.")
                break
        except ValueError:
            print("Please enter a valid number.")
        guesses_left -= 1
        if guesses_left == 0:
            print(
                f"😔Sorry, you've run out of guesses. The number was {number}.")


guess_the_number()
