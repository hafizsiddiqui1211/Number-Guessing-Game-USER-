# Guess The Number Game

## Introduction
This is a simple **Guess the Number** game where the computer randomly selects a number between **0 and 100**, and the player has **7 chances** to guess the correct number.

## How to Play
1. Run the script.
2. The game will generate a random number between **0 and 100**.
3. You have **7 attempts** to guess the correct number.
4. After each incorrect guess, you will receive a hint:
   - **"Too low! Try again."** (if your guess is smaller than the number)
   - **"Too high! Try again."** (if your guess is greater than the number)
5. If you guess the correct number, you win 🎉.
6. If you fail to guess within 7 attempts, the game will reveal the number.

## Requirements
- Python 3.x

## How to Run
1. Ensure you have Python installed.
2. Save the script as `guess_the_number.py`.
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using:
   ```bash
   python guess_the_number.py
   ```

## Example Gameplay
```
Welcome to the number Guessing Game
I'm thinking of a number between 0 and 100. You have 7 tries to guess it.
You've 7 guesses left.
Enter your guess: 50
Too low! Try again.
...
🎉 Congratulations! You guessed the number 42 correctly.
```

## License
This project is open-source and free to use.

