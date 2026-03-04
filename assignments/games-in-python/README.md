# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game using Python. In this assignment, you will practice string manipulation, loops, conditionals, and user input while creating a complete playable program.

## 📝 Tasks

### 🛠️	Set Up the Game Logic

#### Description
Create the core Hangman setup by selecting a random word from a predefined list and displaying the hidden word as underscores.

#### Requirements
Completed program should:

- Define a list of possible words and randomly choose one at the start of the game.
- Display the current word progress using underscores for unknown letters.
- Accept one letter guess from the player each turn.
- Update the displayed progress when the guessed letter is in the word.


### 🛠️	Implement Win/Lose Flow

#### Description
Finish the game loop by tracking incorrect guesses, checking for game-over conditions, and displaying a final result message.

#### Requirements
Completed program should:

- Track and reduce remaining attempts when a guessed letter is not in the word.
- End the game with a win message when all letters in the word are revealed.
- End the game with a lose message when attempts reach zero.
- Reveal the correct word when the player loses.
