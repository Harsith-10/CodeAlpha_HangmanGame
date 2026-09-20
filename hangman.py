import random

def play_hangman():
    words = ["python", "developer", "coding", "software", "alpha"]
    secret_word = random.choice(words)
    guessed_letters = set()
    max_attempts = 6
    incorrect_guesses = 0

    print("=== Welcome to Hangman ===")

    while incorrect_guesses < max_attempts:
        # Build masked word representation
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Remaining incorrect attempts: {max_attempts - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabet.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            # Check win condition
            if set(secret_word).issubset(guessed_letters):
                print(f"\nCongratulations! You won! The word was: {secret_word}")
                return
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
