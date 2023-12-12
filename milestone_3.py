import random

def check_guess_in_word(guess, secret_word):
    # Checks if the guessed letter is in the secret word
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
        return True
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False

def get_valid_letter():
    # Function to get a valid letter guess from the user
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

def play_game(secret_word):
    # Function to initiate the game
    while True:
        user_guess = get_valid_letter()
        if check_guess_in_word(user_guess, secret_word):
            break

def main():
    secret_words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    secret_word = random.choice(secret_words)

    play_game(secret_word)

if __name__ == "__main__":
    main()

