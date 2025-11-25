import random

# List of predefined words
words = ["python", "hangman", "program", "engineer", "science"]

# Randomly select a word
secret_word = random.choice(words)
guessed_letters = [] 
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Game loop
while wrong_guesses < max_wrong:
    # Show current progress
    display_word = ""
    for char in secret_word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    print("\n Word:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", secret_word)
        break

    # Player input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Correct guess
    if guess in secret_word:
        print("Good job! Letter is in the word.")
        guessed_letters.append(guess)
    else:
        # Wrong guess
        wrong_guesses += 1
        print("Wrong guess!", f"Attempts left: {max_wrong - wrong_guesses}")

# If player loses
if wrong_guesses == max_wrong:
    print("\n Game Over!")
    print("The word was:", secret_word)
