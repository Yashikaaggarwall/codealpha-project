import random

# ASCII art for hangman stages
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

WORDS = ["apple", "tiger", "chair", "python", "cloud"]

def choose_word():
    """Randomly select a word from predefined list."""
    return random.choice(WORDS)

def display_progress(word, guessed_letters):
    """Return the word with underscores for unguessed letters."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main Hangman game function."""
    word = choose_word()
    guessed_letters = []
    wrong_attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman (Pro Version)!")
    print(HANGMAN_PICS[0])
    print(display_progress(word, guessed_letters))

    while wrong_attempts < max_attempts:
        guess = input("\nGuess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter.")
            continue

        # Check duplicate guess
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in word:
            print("✅ Good guess!")
            print(HANGMAN_PICS[wrong_attempts])
            print(display_progress(word, guessed_letters))

            if all(letter in guessed_letters for letter in word):
                print("\n🎉 Congratulations! You guessed the word:", word)
                break
        else:
            wrong_attempts += 1
            print("❌ Wrong guess!")
            print(HANGMAN_PICS[wrong_attempts])
            print(f"Attempts left: {max_attempts - wrong_attempts}")
            print(display_progress(word, guessed_letters))
    else:
        print("\n💀 Game Over! The word was:", word)

def main():
    """Loop game until user quits."""
    while True:
        hangman()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing Hangman!")
            break

# Run the program
if __name__ == "__main__":
    main()
